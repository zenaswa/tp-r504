#!/bin/bash

docker network create tplb

docker build -t im-nginx-lb -f tp-A/Dockerfile tp-A/

mkdir -p shared1 shared2


echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html

docker run -d --name nginx1 -v "/home/fi26-zenas/tp-r504/TP-LB/shared1:/usr/share/nginx/html" -p 81:80 --network tplb --rm nginx:latest
docker run -d --name nginx2 -v "/home/fi26-zenas/tp-r504/TP-LB/shared2:/usr/share/nginx/html" -p 82:80 --network tplb --rm nginx:latest

docker run -d --name im-nginx-lb -p 83:80 --network tplb im-nginx-lb 
