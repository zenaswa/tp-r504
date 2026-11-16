#!/bin/bash

docker stop nginx1 nginx2 im-nginx-lb
docker rm im-nginx-lb

docker network rm tplb