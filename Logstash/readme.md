## Logstash

docker build -t nimdoc/logstash:0.1 .

docker run -p 8123:8080 nimdoc/logstash:0.1

docker run --rm -p 8123:8080 -e OBSERVER=observer -e LSNAME=ls01 -e NEXT_CONTAINER=ls02 --name=ls01 --network="longstache" --network="longstache" nimdoc/logstash:0.1

## Node app

docker run --rm -it -v ${PWD}:/home/node/app node bash

docker run --rm -p  3005:3001 -it --name="observer" --network="longstache" -v ${PWD}:/home/node/app node bash

## Docker stuff

### Stop all the containers

docker stop $(docker ps -a -q)

### Remove all the containers

docker rm $(docker ps -a -q)

