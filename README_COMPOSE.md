# Dragonfly Tutorial -- Docker Compose Edition

## Notes

* Commands on the host will start with the `>` prompt.  Commands in a container will start with the `#` prompt.
* Broker information is stored in the YAML file `$HOME/.dripline_mesh.yaml`
* Authentication information is provided with environment variables
* We're using the `develop-dev` information.  For reduced verbosity (no DEBUG or TRACE printouts available), 
  smaller images, and "faster" processing, you can use the `develop` image.

## Setup

1. Open three terminal windows & start Docker
2. Clone the repository
  ```
  > git clone git@github.com:nsoblath/dragonfly_tutorial
  ```
2. Start up the "infrastructure" containers
  ```
  > docker compose -f docker-compose.yaml -f docker-compose-services.yaml up -d rabbit-broker postgres scpi-device
  ```
3. Check the Docker services' status with `ps` or `logs`
  ```
  > docker compose -f docker-compose.yaml -f docker-compose-services.yaml ps
  > docker compose -f docker-compose.yaml -f docker-compose-services.yaml logs postgres
  ```

## Dripline Mesh

1. Start the `key-value-store` (software-only service), `scpi-service` (talks to `cpi-device`), and `sensor-logger` (puts logged data in the database)
  ```
  > docker compose -f docker-compose.yaml -f docker-compose-services.yaml up -d key-value-store scpi-service sensor-logger
  ```
2. Check the Docker services' status with `ps` or `logs`

## Monitoring & Interacting

* Check the RabbitMQ Broker web interface.  In a browser on your host machine go to `localhost:15672`
* Monitor messages with `dl-mon
  ```
  > docker compose -f docker-compose.yaml -f docker-compose-services.yaml up dl-mon
  ```
  This configuration will watch for sensor logging messages on the alerts exchange -- those that should be recieved by the `sensor-logger`.
* Get a value
  ```
  > docker compose -f docker-compose.yaml -f docker-compose-services.yaml run key-value-store bash
  ```
  ```
  # dl-agent get peaches
  ```
* Set a value
  ```
  # dl-agent set peaches 5.3
  # dl-agent get peaches
  ```
