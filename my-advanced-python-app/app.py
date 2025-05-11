# app.py
from flask import Flask
import os
import datetime

app = Flask(__name__)

# Get environment variables or set defaults
app_version = os.environ.get('APP_VERSION', '0.0.1') # Default version if not set
author_name = os.environ.get('AUTHOR_NAME', 'Gishant') # Default author if not set
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def hello():
    message = f"Hello from {author_name}'s Flask App in Docker! (v{app_version})<br>"
    message += f"The current server time is: {current_time}<br>"
    message += "This is awesome!"
    return message

if __name__ == '__main__':
    # Run the app on 0.0.0.0 to be accessible outside the container
    # and on port 5000 (a common port for Flask apps)
    app.run(host='0.0.0.0', port=5000, debug=True)
