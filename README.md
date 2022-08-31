# REST_API_DOCKER 

poster/poster.py
Listens to POST requests
Redirects data from POSTs to Rabbitmq

saver/saver.py
Consumes Rabbitmq queue
Saves incoming data to Redis

explorer/explorer.py
Listens to GET requests @ /size
Returns the count of all keys in Redis


# Requirements

Docker bridge
$ docker network create <network-name>
Redis port 6379 & name=redis by default
Rabbitmq  port 5672 & name=rabbitmq by default
