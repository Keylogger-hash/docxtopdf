#!/bin/bash


sudo docker container rm $(sudo docker container ls -aq) --force

sudo docker image rm $(sudo docker image ls -aq)

sudo docker volume rm $(sudo docker volume ls -a)
