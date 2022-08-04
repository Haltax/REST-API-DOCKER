from flask import Flask, request
import redis
from configparser import ConfigParser


#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the redis ip and port
redisinfo = config_object["Redis"]
redis_host = format(redisinfo["Redis_IP"])
redis_port=format(redisinfo["Redis_port"])


r=redis.StrictRedis(host=redis_host,port=redis_port, decode_responses = True)

app = Flask(__name__)

@app.route('/size', methods=["GET"])

#Get the size of keys in redis

def get_size():
    size=r.dbsize()
    return str(size)
            


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)

