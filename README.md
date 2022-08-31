# REST_API_DOCKER 

poster/poster.py <br />
Listens to POST requests <br />
Redirects data from POSTs to Rabbitmq <br />

saver/saver.py <br />
Consumes Rabbitmq queue <br />
Saves incoming data to Redis <br />
 
explorer/explorer.py <br />
Listens to GET requests @ /size <br />
Returns the count of all keys in Redis <br />


# Requirements <br />

Docker bridge <br />
$ docker network create <network-name> <br />
Redis port 6379 & name=redis by default  <br />
Rabbitmq  port 5672 & name=rabbitmq by defaul <br />
