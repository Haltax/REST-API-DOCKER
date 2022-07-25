from flask import Flask, request
import redis

redis_host = input("Enter the redis_host ip: ")
redis_port = int(input("Enter the redis port: "))
api_port = int(input("Enter the web port: "))


r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

app = Flask(__name__)


@app.route('/size', methods=["GET"])
def get_size():
    size = r.dbsize()
    return str(size)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=api_port)
