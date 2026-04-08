import os
import socket
import redis
from flask import Flask, jsonify

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))

cache = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def get_hit_count():
    try:
        return cache.incr("hits")
    except redis.exceptions.ConnectionError:
        return "Redis not ready"

@app.route("/")
def home():
    count = get_hit_count()
    return f"""
    <html>
      <head><title>Docker Compose DevOps Project</title></head>
      <body>
        <h1>Docker Compose Reverse Proxy Project</h1>
        <p>This request has been processed through Nginx to Flask.</p>
        <p>Hostname: {socket.gethostname()}</p>
        <p>Visits: {count}</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
