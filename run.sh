#!/bin/bash
mkdir -p /docker/volume/delay/media
docker container stop delay
docker rm delay
docker rmi delay-image
docker build -t delay-image .
docker run \
--name delay \
-v /docker/volume/delay/media:/home/app/webapp/media \
--net tashmediatrans-network \
-p 2005:2005 \
-d \
delay-image