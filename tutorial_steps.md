# Dragonfly Tutorial

In this tutorial we'll go through a scenario in which we'll simulate establishing and developing an experimental lab setup. 
The tutorial has an intial setup stage, and then three tutorial stages.

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

By the end of this setup, you will have the following:

* Three directories:
  * `dragonfly_tutorial`: clone of the `project8/dragonfly_tutorial` repo, which will provide the source information for this tutorial
  * `dragonfly`: clone of the `project8/dragonfly` repo, which we'll be modifying to add code that will address the laboratory setup in our scenario.
  * `workspace`: this will represent the repo in which the configuration details for our laboratory setup live.
* A Docker Swarm that consists of just the host machine that you're working on.
* A Docker network that will be used to communicate between all of our services.

0. Start in a directory that, for the purposes of these instructions, we'll call `top`.  All of our tutorial material will go in this directory.  On your machine it could be a dedicated directory that you create for going through this tutorial, or some other location.
1. Clone dragonfly_tutorial into the `top` directory
  ```
  > git clone git@github.com:project8/dragonfly_tutorial
  ```
2. Clone dragonfly into the `top` directory and choose the right branch
  ```
  > git clone git@github.com:project8/dragonfly
  > cd dragonfly
  > git checkout with-hbmon
  ```
3. Create your `workspace` directory and two subdirectories, and copy in pre-made docker-compose and dripline config files
  ```
  > cd ..
  > mkdir workspace
  > cp dragonfly_tutorial/docker workspace
  > cp dragonfly_tutorial/services workspace
  > cp dragonfly_tutorial/infrastructure workspace
  ```
4. Create the swarm on the primary node.  For this tutorial, we'll be running on a single node, so the IP can be the localhost, `127.0.0.1`.
  ```
  > docker swarm init --advertise-addr 127.0.0.1
  ```
5. Create an overlay network.  This is what the services will use to communicate with each other.  The `attachable` attribute means that other containers can be added, e.g. to do diagnostics on the fly.  Run this on the primary node.  For the `[name]` argument, we suggest using `mesh`, and that's what's assumed in the relevant YAML files included in this repository.
  ```
  > docker network create \
    --attachable \
    --driver overlay \
    [name]
  ```


## Stage 1

1. Start with the infrastructure services:
  ```
  > docker stack deploy --compose-file docker/docker-compose-infra-1.yaml infra-1
  ```
  Ensure that they are running stably.
2. Open web pages
  * RabbitMQ management @ `localhost:15672`
  * SlowDash @ `localhost:18881`
3. Deploy the services in `docker-compose-services-1.yaml
  ```
  > docker stack deploy --compose-file docker/docker-compose-services-1.yaml serv-1
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
  2. Copy `dragonfly_tutorial/templates/scpi-service-template.yaml` to `workspace/services/scpi-device-service.yaml`
  3. Fill in the endpoints according to the commands
2. Create the container specification for the SCPI device service
  1. Copy `dragonfly_tutorial/templates/docker-compose-services-X.yaml` to `workspace/docker/docker-compose-services-2.yaml`
  2. Fill in the missing information indicated by angle brackets (`<...>`)
3. Deploy the new service
  ```
  > docker stack deploy --compose-file docker/docker-compose-services-2.yaml serv-2
  ```
4. Verify that the service is stably running
  * You should see the channel on the rabbitmq website
  * The heartbeats should be monitored after the first  is sent
  * If any values are being logged, you should be able to see them in Slow Dash
5. Perform get and set requests using `dl-agent`


## Stage 3

1. Create your custom code and add your code to `dragonfly/dripline/extensions` and edit `__init__.py`
2. Create the config file for the SCPI device
  1. Use the `unusual_device/manual.md` to know the available commands
  2. Copy `dragonfly_tutorial/templates/scpi-service-template.yaml` to `workspace/services/unusual-device-service.yaml`
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

