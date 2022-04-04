#!/bin/sh
# Create an initial DB in mongodb from CSV files

PORT=27017

cp ../../files/*.csv.gz ./data/
docker build -t mongo-seed -f Dockerfile-seed .


docker rm mongo-sub mongo-seed -f

docker run --name mongo-sub -d -p $PORT:27017 mongo:5.0.6-focal

docker run --link mongo-sub:mongodb --name mongo-seed mongo-seed

echo "Done. DB ready listening at $PORT!"
