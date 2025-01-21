# Dragonfly Tutorial

## Objectives

1. Workflow for dragonfly development
2. Deployment of a dragonfly mesh with Docker Swarm
  1. Infrastructure: broker, database
  2. Services: dl-mon, heartbeat monitor, key-value-store, SCPI device, unusual SCPI device
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
4. Edit the docker-compose files to refer to the