# compose-example/webapp/app.py
from flask import Flask
import os
import datetime
import redis # Import the redis library

app = Flask(__name__)

# Connect to Redis.
# We use the service name 'redis' as the hostname, Docker Compose will handle DNS.
# The default Redis port is 6379.
try:
    # We'll use the service name 'redis' as hostname, as defined in docker-compose.yml
    r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
    r.ping() # Check connection
    redis_connected = True
except redis.exceptions.ConnectionError as e:
    redis_connected = False
    redis_error_message = str(e)


app_version = os.environ.get('APP_VERSION', '0.0.1-compose-default')
author_name = os.environ.get('AUTHOR_NAME', 'Gishant with Compose Default')

@app.route('/')
def hello():
    page_hits = 0
    if redis_connected:
        try:
            page_hits = r.incr('page_hits') # Increment counter in Redis
        except redis.exceptions.RedisError as e:
            # Handle potential error if redis becomes unavailable after initial connect
            return f"Error connecting to Redis during increment: {str(e)}"
    else:
        # Could display an error or fallback content if Redis isn't connected
        return f"<h1>Error: Could not connect to Redis.</h1><p>{redis_error_message}</p>"


    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"<h1>Hello from {author_name}'s Flask App with Redis!!</h1>"
    html += f"<p>App Version: {app_version}</p>"
    html += f"<p>The current server time is: {current_time}</p>"
    if redis_connected:
        html += f"<h2>This page has been viewed {page_hits} times.</h2>"
    else:
        html += f"<h2>Redis counter is unavailable.</h2>"
    html += "<p>Powered by Docker Compose!</p>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
