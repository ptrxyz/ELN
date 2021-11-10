# ELN

This initial project implements an integrated solution to setup and run Docker images of the Chemotion ELN

The central script that builds the required images is CI.sh.

After the image is successfully built the image can be shipped and started with the docker-compose.yml file. The local setup has to be performed with setup.sh.

Required software for building the docker images:
* python3
* python-click
* python-yaml
* curl
* git
* docker, docker-compose
