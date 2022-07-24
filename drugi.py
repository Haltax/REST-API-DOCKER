import pika
import redis


rabbitmq_host = input("Enter the rabbitmq_host ip: ")
rabbitmq_queue = input("Enter the queue: ")
redis_host = input("Enter the redis_host ip: ")
redis_port = int(input("Enter the redis port: "))

TTL = 60
counter = 0


print(' [*] Connecting to server ...')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue=rabbitmq_queue)

print(' [*] Waiting for messages.')

r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)


def callback(ch, method, properties, body):

    tmp = str(body)
    global counter

    if(r.setnx(counter, tmp) == 1):
        r.set(counter, tmp)
        r.expire(counter, TTL)

    else:

        while r.setnx(counter, tmp) == 0:

            r.setnx(counter, tmp)
            r.expire(counter, TTL)
            counter += 1

        counter = 0

    print(tmp)

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=rabbitmq_queue, on_message_callback=callback)
channel.start_consuming()
