# compose-example/webapp/Dockerfile

# 1. Specify the base image
FROM python:3.9-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_VERSION="1.0-compose"
ENV AUTHOR_NAME="Gishant with Compose"

# 3. Set the working directory inside the image
WORKDIR /app

# 4. Copy requirements.txt first
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY . .

# 7. Expose the port the app runs on
EXPOSE 5000

# 8. Specify the default command to run when the container starts
CMD ["python", "./app.py"]
