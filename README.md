# application

git clone https://github.com/Haltax/application.git

pip3 install pika
pip3 install flask

docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3.6-management-alpine

docker network create -d bridge redisnet

docker run -d -p 6380:6380 --name myredis --network redisnet redis

python pierwszy.py
python drugi.py
python trzeci.py
