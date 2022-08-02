from flask import Flask, request
import pika
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--rabbit_ip", default="127.0.0.1", help="Rabbitmq IP address")
parser.add_argument("-q", "--queue", default="new", help="Rabbitmq queue name")
args = vars(parser.parse_args())

rabbitmq_host = args["rabbit_ip"]
rabbitmq_queue = args["queue"]


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue=rabbitmq_queue)

app = Flask(__name__)

@app.route('/add', methods=["POST"])

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
    app.run(debug=True, host='0.0.0.0')
