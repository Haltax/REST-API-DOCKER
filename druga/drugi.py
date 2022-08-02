import pika
import redis
import configparser

#get variables from config file
config = configparser.ConfigParser()
config.read=('config.env')
rabbitmq_host = config.get('Rabbitmq','Rabbit_IP')
rabbitmq_queue = config.get('Rabbitmq','Rabbit_queue')
redis_host = config.get('Redis','Redis_IP')
redis_port=config.get('Redis','Redis_port')


#live time for objects in redis
TTL=60

#for the keys in redis
counter=0


#Connect to rabbitmq server

print(' [*] Connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue=rabbitmq_queue)

print(' [*] Waiting for messages.')

r=redis.StrictRedis(host=redis_host,port=redis_port, decode_responses = True)



def callback(ch, method, properties, body):
    
    tmp=str(body)
    global counter

  #check from key 0 if it exists

    while r.setnx(counter,tmp) == 0:
            
        r.setnx(counter,tmp)
        r.expire(counter, TTL)
        counter+=1
             
    counter=0


    
    print(tmp)
    
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=rabbitmq_queue, on_message_callback=callback)
channel.start_consuming()
