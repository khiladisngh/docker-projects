# Docker Commands Cheatsheet

Based on "Docker Course Notes (Detailed)"

## Lesson 1.2: Introduction to Docker

**Commands Reference**
* `docker build ...`: Builds an image from a Dockerfile.
* `docker run ...`: Runs a command in a new container.
* `docker ps`: Lists running containers.
* `docker pull <image_name>`: Downloads an image from a registry.
* `docker push <image_name>`: Uploads an image to a registry.
* `docker login`: Logs into a Docker registry.

## Lesson 1.3: Setting Up the Docker Development Environment

**Commands Reference**
* `sudo usermod -aG docker $USER`: (Linux) Adds your user to the `docker` group to run Docker commands without `sudo`. Requires logout/login.
* `docker --version`: Displays the installed Docker version.
* `docker info`: Displays system-wide information about the Docker installation.
* `docker run hello-world`: Pulls (if not present) and runs the `hello-world` image as a quick test of the Docker installation.

## Lesson 1.4: Working with Docker Images

**Commands Reference**
* `docker pull <image_name>[:<tag>]`: Downloads an image (e.g., `hello-world`) from a registry (default: Docker Hub).
* `docker images`: Lists all images stored locally on your Docker host.
* `docker run <image_name>[:<tag>]`: Creates and starts a new container from the specified image. Pulls the image if not found locally.
* `docker ps`: Lists currently running containers.
* `docker ps -a` (or `docker ps --all`): Lists all containers, including those that are stopped or have exited.

## Lesson 1.5: Managing Containers

**Commands Reference**
* `docker ps`: Lists currently running containers.
* `docker ps -a`: Lists all containers (running, stopped, exited).
* `docker rm <container_id_or_name> ...`: Removes one or more stopped containers.
* `docker container prune`: Removes all stopped containers.
* `docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>`: Runs a container in detached mode, with port mapping and a specific name (e.g., `docker run -d -p 8080:80 --name my-webserver nginx`).
* `docker logs <container_id_or_name>`: Fetches the logs of a container.
* `docker logs -f <container_id_or_name>`: Follows the log output of a container in real-time.
* `docker stop <container_id_or_name> ...`: Stops one or more running containers.
* `docker start <container_id_or_name> ...`: Starts one or more stopped containers.
* `docker restart <container_id_or_name> ...`: Restarts one or more containers.
* `docker exec -it <container_id_or_name> <command>`: Executes a command in an interactive terminal inside a running container (e.g., `docker exec -it my-webserver bash`).
* `docker exec <container_id_or_name> <command>`: Executes a command inside a running container.
* `docker rmi <image_name_or_id> ...`: Removes one or more images (if not used by any containers).
* `docker image prune`: Removes dangling images (layers not associated with any tagged image).
* `docker image prune -a`: Removes all unused images (not just dangling ones).

## Lesson 1.6: Building Your First Docker Image (Dockerfile Basics)

**Dockerfile Instructions Introduced**
* `FROM <base_image>:<tag>`: Specifies the base image for the build.
* `WORKDIR /path/in/image`: Sets the working directory for subsequent instructions.
* `COPY <source_on_host> <destination_in_image>`: Copies files/directories from the build context into the image.
* `CMD ["executable", "param1", ...]` : Specifies the default command to run when the container starts.

**Commands Reference**
* `mkdir <directory_name>`: (OS command) Creates a new directory.
* `cd <directory_name>`: (OS command) Changes the current directory.
* `docker build -t <image_name>:<tag> <path_to_build_context>`: Builds a Docker image from a Dockerfile.
    * Example: `docker build -t gishant-python-app .`
* `docker images`: Lists locally stored Docker images.
* `docker run <image_name>:<tag>`: Runs a container from the specified custom image.
    * Example: `docker run gishant-python-app`

## Lesson 1.7: More Dockerfile Instructions & Best Practices

**Dockerfile Instructions Introduced**
* `ENV <KEY>=<VALUE>`: Sets environment variables in the image.
* `RUN <command>`: Executes commands during the image build process (e.g., installing packages).
* `EXPOSE <port>/<protocol>`: Documents the port(s) the application inside the container listens on. Does not publish the port.

**Commands Reference**
* `docker build -t <image_name>:<tag> .`: Builds the Docker image (as in previous lesson).
    * Example: `docker build -t gishant-flask-app:v1 .`
* `docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>:<tag>`: Runs the container with port mapping.
    * Example: `docker run -d -p 5001:5000 --name my-flask-webapp gishant-flask-app:v1`
* `docker logs <container_name>`: Views logs of the specified container.
* `docker stop <container_name>`: Stops the specified container.
* `docker rm <container_name>`: Removes the specified (stopped) container.

## Lesson 1.8: Docker Volumes and Persistent Data

**Commands Reference**
* `docker volume create <volume_name>`: Creates a new named Docker volume.
    * Example: `docker volume create my-persistent-data`
* `docker volume ls`: Lists all Docker volumes.
* `docker volume inspect <volume_name>`: Displays detailed information about a specific volume.
* `docker run --mount source=<volume_name>,target=<path_in_container> <image_name> ...`: Mounts a named volume into a container.
    * Example: `docker run --rm --mount source=my-persistent-data,target=/data alpine sh -c "echo 'Hi' > /data/file.txt"`
* `docker run --mount type=bind,source=<host_path>,target=<path_in_container> <image_name> ...`: Mounts a host directory/file into a container (bind mount).
    * Example: `docker run -d --mount type=bind,source="$(pwd)",target=/app gishant-flask-app:v1`
* Shorthand for mounts: `-v <volume_name_or_host_path>:<path_in_container>`
* `docker volume rm <volume_name>`: Removes a specific Docker volume (if not in use).
* `docker volume prune`: Removes all unused (dangling) local volumes.

## Lesson 1.9: Docker Networking Basics

**Commands Reference**
* `docker network create <network_name>`: Creates a new user-defined Docker network (typically bridge by default).
    * Example: `docker network create my-app-network`
* `docker network ls`: Lists all Docker networks on the host.
* `docker network inspect <network_name>`: Displays detailed information about a specific network.
* `docker network rm <network_name>`: Removes a user-defined network (if no containers are connected).
* `docker run --network <network_name> ...`: Connects a new container to the specified network at startup.
    * Example: `docker run -d --name web-server --network my-app-network nginx`
* `docker network connect <network_name> <container_name_or_id>`: Connects an existing, running container to an additional network.
* `docker network disconnect <network_name> <container_name_or_id>`: Disconnects a container from a network.
* (Inside Alpine container) `apk update`: Updates package lists.
* (Inside Alpine container) `apk add <package_name>`: Installs a package (e.g., `apk add curl`).
* (Inside container) `ping -c 3 <container_name>`: Pings another container by its name on the same user-defined network.
* (Inside container) `curl http://<container_name>`: Accesses an HTTP service on another container by its name.

## Lesson 1.10: Introduction to Docker Compose

**Commands Reference**
* `docker compose version`: Displays the Docker Compose version.
* `docker compose up [options] [<service_name>...]`: Builds (if needed), creates, starts, and attaches to containers for services defined in `docker-compose.yml`.
    * `docker compose up -d`: Runs services in detached (background) mode.
    * `docker compose up --build`: Forces a rebuild of images before starting services.
* `docker compose down [options]`: Stops and removes containers, networks, and optionally volumes.
    * `docker compose down -v`: Removes named volumes along with containers and networks.
* `docker compose ps`: Lists the status of containers for the current Compose project.
* `docker compose logs [options] [<service_name>...]`: Displays logs from services.
    * `docker compose logs -f <service_name>`: Follows log output in real-time.
* `docker compose build [<service_name>...]`: Builds or rebuilds images for services.
* `docker compose pull [<service_name>...]`: Pulls the latest images for services.
* `docker compose exec <service_name> <COMMAND> [ARG...]`: Executes a command inside a running container of a service.
    * Example: `docker compose exec web bash`
* `docker compose stop [<service_name>...]`: Stops running services without removing them.
* `docker compose start [<service_name>...]`: Starts existing, stopped services.
* `docker compose restart [<service_name>...]`: Restarts services.
* `docker compose config`: Validates and views the effective Compose configuration.
* `docker compose top [<service_name>...]`: Displays the running processes for services.
