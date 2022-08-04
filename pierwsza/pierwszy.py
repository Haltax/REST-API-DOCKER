from flask import Flask, request
import pika
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the rabbit ip and queue
rabitinfo = config_object["Rabbit"]
rabbitmq_host=format(rabitinfo["Rabbit_IP"])
rabbitmq_queue=format(rabitinfo["Rabbit_queue"])

#connect to rabbitmq server

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue=rabbitmq_queue)

app = Flask(__name__)

@app.route('/add', methods=["POST"])

#function that checks if input is json type

def process_json():
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):


        json=request.json
        tmp=str(json)
        channel.basic_publish(exchange='', routing_key=rabbitmq_queue, body=tmp)


        return json


    else:
        return '400 Bad Request'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)

