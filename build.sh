#!/bin/sh

docker build -t depositapp .

docker rm depositapp

docker run -d --name depositapp  -p 8000:8000 depositapp
