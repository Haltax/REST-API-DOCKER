from flask import Flask, request
import redis
import configparser

#get variables from config file
config = configparser.ConfigParser()
config.read=('config.env')
redis_host = config.get('Redis','Redis_IP')
redis_port=config.get('Redis','Redis_port')


r=redis.StrictRedis(host=redis_host,port=redis_port, decode_responses = True)

app = Flask(__name__)

@app.route('/size', methods=["GET"])

def get_size():
    size=r.dbsize()
    return str(size)
            


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)

