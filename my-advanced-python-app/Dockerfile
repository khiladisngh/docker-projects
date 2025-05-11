# Dockerfile for Flask App

# 1. Specify the base image
FROM python:3.9-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_VERSION="1.0-dockerized"
ENV AUTHOR_NAME="Gishant Singh"

# 3. Set the working directory inside the image
WORKDIR /app

# 4. Copy the requirements file first (for better layer caching)
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY . .
# This copies everything from the build context's current directory (.)
# into the image's WORKDIR (/app). Since requirements.txt is already copied,
# this will copy app.py and any other files.

# 7. Expose the port the app runs on (documentation, does not publish the port)
EXPOSE 5000

# 8. Specify the command to run when the container starts
CMD ["python", "./app.py"]
