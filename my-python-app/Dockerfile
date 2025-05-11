# Dockerfile

# 1. Specify the base image
FROM python:3.9-slim

# 2. Set the working directory inside the image
WORKDIR /app

# 3. Copy our Python script into the image's working directory
COPY app.py .

# 4. Specify the command to run when the container starts
CMD ["python", "./app.py"]
