# REST_API_DOCKER 

poster/poster.py \n
Listens to POST requests \n
Redirects data from POSTs to Rabbitmq \n

saver/saver.py \n
Consumes Rabbitmq queue \n
Saves incoming data to Redis \n
 
explorer/explorer.py \n
Listens to GET requests @ /size \n
Returns the count of all keys in Redis \n


# Requirements \n

Docker bridge \n
$ docker network create <network-name> \n
Redis port 6379 & name=redis by default  \n
Rabbitmq  port 5672 & name=rabbitmq by defaul \n
