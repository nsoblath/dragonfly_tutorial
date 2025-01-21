# Dragonfly Tutorial

## Notes

* There are two different uses of the word "service" when we combind Docker Swarm (or Compose) with Dripline.  In Dripline, a service is the element of a mesh that is the interface between an instrument or piece of software and the mesh itself.  In the Docker realm, a service is a container running as part of a Compose setup or a Swarm.  
* We're going to be very explicit about our network setup.  We'll specify the subnet (i.e. the IP address range) to be `10.0.1.0` --> `10.0.1.255`, and we'll specify the IP address of certain Docker services so that we can address them properly.

## Setup

1. Create the swarm on the primary node.  For this tutorial, we'll be running on a single node, so the IP can be the localhost, `127.0.0.1`.
  ```
  docker swarm init --advertise-addr 127.0.0.1
  ```
2. If you want to add more nodes to your swarm, you would run the following command on the node(s) you're adding.  The full version of this command should be printed to the terminal by the `docker swarm init` command above.  If you're just using a single node, you can skip this step.
  ```
  docker swarm join --token [token]
  ```
3. Create an overlay network.  This is what the services will use to communicate with each other.  The `attachable` attribute means that other containers can be added, e.g. to do diagnostics on the fly.  Run this on the primary node.  For the `[name]` argument, we suggest using `mesh`, and that's what's assumed in the relevant YAML files included in this repository.
  ```
  docker network create \
    --attachable \
    --driver overlay \
    --subnet 10.0.1.0\24 \
    --gateway 10.0.1.1 \
    [name]
  ```

## Deploy Services

1. Start with the infrastructure services:
  ```
  > docker stack deploy --compose-file docker-compose-infra.yaml infra
  ```
  Ensure that they are running stably.
2. Open web pages
  * RabbitMQ management @ `localhost:15672`
  * SlowDash @ `localhost:18881`
  * DL Agent @ `localhost:8080/web/agent.html`
3. Then start the dripline services:
  ```
  > docker stack deploy --compose-file docker-compose-services.yaml services
  ```

## Interact with Things

* Add a new plot to SlowDash
  1. Select Add a New Plot
  2. Select Add a New Pannel
  3. Channel (pulldown): peaches
  4. Select Create
  5. Change the auto-update time to 30 seconds
* ~~Get a value with the DL Agent web page~~
  1. Select Type: GET
  2. Fill in Routing Key: `peaches`
* Get a value using the CL
  1. Start a new interactive container with a bash shell and attach it to the `mesh` network
    ```
    > docker run -it --rm --network mesh ghcr.io/driplineorg/dripline-python:latest bash
    ```
  2. Get the value of `peaches`
    ```
    # dl-agent get -b rabbit-broker -u dripline --password dripline peaches
    ```
  3. Get the IDN string from the SCPI Device
    ```
    # dl-agent get -b rabbit-broker -u dripline --password dripline idn
    ```
* Set a value and see the change
  1. Set the value of `peaches`
    ```
    # dl-agent set -b rabbit-broker -u dripline --password dripline peaches 5
    ```
  2. Check on SlowDash to see the change recorded
