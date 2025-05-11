# Docker Projects and Learning Notes

This repository contains a collection of Docker projects and learning notes.

## Projects

### 1. Simple Python App (`my-python-app`)

A basic Python application that prints a greeting message, the current time, and a custom message. This project demonstrates a minimal `Dockerfile` setup.

- **[my-python-app/app.py](my-python-app/app.py)**: The Python script.
- **[my-python-app/Dockerfile](my-python-app/Dockerfile)**: Dockerfile to containerize the Python script.

**To build and run:**
```sh
cd my-python-app
docker build -t my-python-app .
docker run my-python-app
```

### 2. Advanced Python Flask App (`my-advanced-python-app`)

A Flask web application that displays a greeting, application version, author name, and the current server time. This project showcases more advanced `Dockerfile` features, including:
- Setting environment variables (`ENV`).
- Installing dependencies from `requirements.txt`.
- Using `.dockerignore` for an optimized build context.
- Exposing a port.

- **[my-advanced-python-app/app.py](my-advanced-python-app/app.py)**: The Flask application.
- **[my-advanced-python-app/Dockerfile](my-advanced-python-app/Dockerfile)**: Dockerfile for the Flask app.
- **[my-advanced-python-app/requirements.txt](my-advanced-python-app/requirements.txt)**: Python dependencies (Flask).
- **[my-advanced-python-app/.dockerignore](my-advanced-python-app/.dockerignore)**: Specifies files to exclude from the Docker build context.

**To build and run:**
```sh
cd my-advanced-python-app
docker build -t my-advanced-python-app .
docker run -d -p 5000:5000 --name advanced-app my-advanced-python-app
```
Access the application at `http://localhost:5000`.

### 3. Docker Compose Example (`compose-example`)

A multi-container application using Docker Compose, featuring a Flask web application that connects to a Redis database to count page visits.

- **[compose-example/docker-compose.yml](compose-example/docker-compose.yml)**: Defines the `web` (Flask) and `redis` services.
- **`compose-example/webapp/`**: Contains the Flask application.
    - **[compose-example/webapp/app.py](compose-example/webapp/app.py)**: The Flask application code that interacts with Redis.
    - **[compose-example/webapp/Dockerfile](compose-example/webapp/Dockerfile)**: Dockerfile for the Flask web application.
    - **[compose-example/webapp/requirements.txt](compose-example/webapp/requirements.txt)**: Python dependencies (Flask, redis).

**To run with Docker Compose:**
```sh
cd compose-example
docker compose up -d --build
```
Access the web application at `http://localhost:5001`.

**To stop and remove containers:**
(Assuming you are in the `compose-example` directory)
```sh
docker compose down
```
Note: If you have enabled data persistence for Redis by uncommenting the volume sections in the [`compose-example/docker-compose.yml`](compose-example/docker-compose.yml) file, use `docker compose down -v` to also remove the Redis data volume.

## Learning Notes (`notes`)

This directory contains detailed notes on Docker concepts, organized into modules and lessons. These notes cover topics from basic containerization principles to advanced Docker features.

- **[notes/docker_cheatsheet.md](notes/docker_cheatsheet.md)**: A comprehensive cheatsheet and detailed notes covering various Docker lessons.

These notes serve as a reference for understanding Docker concepts and commands.
