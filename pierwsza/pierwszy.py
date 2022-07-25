from flask import Flask, request
import pika


rabbitmq_host = input("Enter the host ip: ")
rabbitmq_queue=input("Enter the queue: ")

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
