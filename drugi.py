import pika
import redis

redis_host='localhost'
redis_port=6379
TTL=60

a=1

print(' [*] Connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='nowa')

print(' [*] Waiting for messages.')


def callback(ch, method, properties, body):
    tmp=str(body)
    a=1
    r=redis.StrictRedis(host=redis_host,port=redis_port, decode_responses = True)


    if(r.setnx(1,tmp)==0):
        r.set(1,tmp)
        r.expire(1,TTL)
    else:
        r.set(a,tmp)
        r.expire(a,TTL)

    
    print(tmp)
    
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='nowa', on_message_callback=callback)
channel.start_consuming()
