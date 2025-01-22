# Dragonfly Tutorial

## Objectives

1. Workflow for dragonfly development
2. Deployment of a dragonfly mesh with Docker Swarm
  1. Infrastructure: broker, database, Slow Dash, SCPI device, (unusual SCPI device)
  2. Services: heartbeat monitor, key-value-store, SCPI device's service, unusual SCPI device's service
3. Mesh development
  1. Adding services
4. Dragonfly development
  1. Creating a new endpoint

## Setup

1. Clone dragonfly_tutorial
  ```
  > git clone git@github.com:project8/dragonfly_tutorial
  ```
2. Clone dragonfly into the dragonfly_tutorial directory and choose the right branch
  ```
  > cd dragonfly_tutorial
  > git clone git@github.com:project8/dragonfly
  > cd dragonfly
  > git checkout with-hbmon
  ```
3. Create your workspace directory and copy in docker-compose files
  ```
  > cd ..
  > mkdir workspace
  > cp docker-compose-infra.yaml workspace
  > cp docker-compose-services-1.yaml workspace
  ```
4. Edit the docker-compose files to refer to the right directories
  * Directory paths to `dragonfly_tutorial` should be to `../` instead of `./`
5. Create the swarm on the primary node.  For this tutorial, we'll be running on a single node, so the IP can be the localhost, `127.0.0.1`.
  ```
  > docker swarm init --advertise-addr 127.0.0.1
  ```
6. Create an overlay network.  This is what the services will use to communicate with each other.  The `attachable` attribute means that other containers can be added, e.g. to do diagnostics on the fly.  Run this on the primary node.  For the `[name]` argument, we suggest using `mesh`, and that's what's assumed in the relevant YAML files included in this repository.
  ```
  > docker network create \
    --attachable \
    --driver overlay \
    [name]
  ```


## Stage 1

1. Start with the infrastructure services:
  ```
  > docker stack deploy --compose-file docker-compose-infra-1.yaml infra-1
  ```
  Ensure that they are running stably.
2. Open web pages
  * RabbitMQ management @ `localhost:15672`
  * SlowDash @ `localhost:18881`
3. Deploy the services in `docker-compose-services-1.yaml
  ```
  > docker stack deploy --compose-file docker-compose-services-1.yaml serv-1
  ```
4. Verify that the expected queues are present in the rabbitmq website
5. Verify that the heartbeat monitor is seeing the expected heartbeats
6. Verify that values are being logged for `peaches` in the KVS
7. Interact with `peaches` using `dl-agent`
  1. Get a bash shell in a dripline-based container
    ```
    > docker exec -it $(docker ps -q -f name=key-value-store) bash
    ```
  2. Send a get request for peaches
    ```
    # dl-agent get peaches
    ```
  3. Set peaches
    ```
    # dl-agent set peaches 5
    ```


## Stage 2

1. Create the config file for the SCPI device
  1. Use the `scpi_device/manual.md` to know the available commands
  2. Copy `templates/scpi-service-template.yaml` to `workspace/services/scpi-device-service.yaml`
  3. Fill in the endpoints according to the commands
2. Create the container specification for the SCPI device service
  * Can be copied from `docker-compose-services-2.yaml` or modeled on the KVS Docker specification
3. Deploy the new service
  ```
  > docker stack deploy --compose-file docker-compose-services-2.yaml serv-2
  ```
4. Verify that the service is stably running
  * You should see the channel on the rabbitmq website
  * The heartbeats should be monitored after the first  is sent
  * If any values are being logged, you should be able to see them in Slow Dash
5. Perform get and set requests using `dl-agent`


## Stage 3

1. Create your custom code and add your code to `workspace/dragonfly/dripline` and edit `__init__.py`
2. Create the config file for the SCPI device
  1. Use the `scpi_device/manual.md` to know the available commands
  2. Copy `templates/scpi-service-template.yaml` to `workspace/services/scpi-device-service.yaml`
  3. Fill in the endpoints according to the commands
3. Run the dev container:
  ```
  > docker run -it --rm --network mesh -v ./dragonfly:/usr/local/src_dev -v ./services/unusual-device-service.yaml:/root/unusual-device.yaml -v ./dripline_mesh.yaml:/root/.dripline_mesh.yaml -e DRIPLINE_USER=dripline,DRIPLINE_PASSWORD=dripline ghcr.io/driplineorg/dripline-python:latest-dev bash
  ```
4. Install dragonfly
  ```
  # pip install /usr/local/src_dev
  ```
5. Try running the service with the new endpoint class
  ```
  # cd /root
  # dl-serve -c unusual-device.yaml
  ```
6. Verify that the service is running stably
7. Debug and reininstall if necessary
  ```
  [on host] edit code
  # pip install /usr/local/src_dev
  # dl-serve -c unusual-device.yaml
  ```
  Repeat as needed
8. Interact with your mesh

