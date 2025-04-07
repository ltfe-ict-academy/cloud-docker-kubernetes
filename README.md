# Cloud Specialization: Docker & Kubernetes

<p align="center">
  <a href="./resources/DockerKubernetes.png"><img src="./resources/DockerKubernetes.png" alt="DockerKubernetes"></a>
</p>
<p align="center">
    <em>Learn Docker and Kubernetes. Learn how to use Docker, Compose and Kubernetes on your machine for better software building and testing.</em>
</p>

![category](https://img.shields.io/badge/category-cloud-orange)
![category](https://img.shields.io/badge/category-docker-orange)
![category](https://img.shields.io/badge/category-kubernetes-orange)
![version](https://img.shields.io/badge/version-v1.0.0-blue)

---

**Live on-site course**: <a href="https://ict-academy.si/usposabljanje/prakticna-delavnica-docker-kubernetes/" target="_blank">https://ict-academy.si/usposabljanje/prakticna-delavnica-docker-kubernetes/</a>

**All courses**: <a href="https://ict-academy.si/" target="_blank">https://ict-academy.si/</a>

---

**What you'll learn**:
- Intro To Docker
- Containers
- Docker Images
- Docker Storage And Volumes
- Docker Networking
- Building Images
- Sharing Docker Images
- Running Multi-container Apps With Docker Compose
- Docker Reliability And Health Checks
- Managing Application Logs
- Monitoring And Management
- Docker Configuration Management
- Docker Security
- Advanced Docker
- Container orchestration and microservices
- Introduction to Kubernetes
- Kubernetes Pods
- Managing the lifecycle of the Pod

## Prerequisites
- Basic understanding of programming
- Basic Familiarity with the command line
- Basic Familiarity with Linux systems

## Full Course Outline

### [Part 1: Intro To Docker](./Part_01_Intro_To_Docker/README.md)
- Containers History
- Introduction to Containers
- Docker overview
- Installing Docker
- Running Hello World in a container
- Example: Running multiple NGINX instances
- Docker Architecture
- The Docker Engine (Advanced)

### [Part 2: Containers](./Part_02_Containers/README.md)
- Containers vs Virtual Machines
- What is a container?
- Starting a simple container
- Container processes
- Web server example
- Exploring the container filesystem and the container lifecycle
- Stopping containers gracefully

### [Part 3: Docker Images](./Part_03_Docker_Images/README.md)
- About Docker Images
- Pulling images
- Image registries
- Image naming and tagging
- Filtering the images on the host
- Images and layers
- Deleting Images

### [Part 4: Docker Storage And Volumes](./Part_04_Docker_Storage_And_Volumes/README.md)
- Introduction to Docker Storage And Volumes
- Containers and non-persistent data
- Running containers with Docker volumes
- Creating and managing Docker volumes
- Demonstrating volumes with containers and services
- Populate a volume using a container
- Use a read-only volume
- Share data between Docker containers
- Use a third party volume driver (Advanced)
- Running containers with filesystem mounts (Bind mounts)
- Limitations of filesystem mounts
- Understanding how the container filesystem is built (Advanced)
- Use tmpfs mounts (Advanced)
- Choose the right type of mount
- Example: Run a PostgreSQL database

### [Part 5: Docker Networking](./Part_05_Docker_Networking/README.md)
- Docker networking overview
- Docker network architecture (Advanced)
- Network drivers
- Bridge networks
- Host network
- Overlay networks
- Connecting to existing networks (Advanced)
- Disable networking for a container
- Port Mapping
- Service discovery (Advanced)
- Docker and iptables (Advanced)

### [Part 6: Building Images](./Part_06_Building_Images/README.md)
- Overview of Docker Build
- Containerizing an app - overview
- Building your first container image
- Understanding Docker images and image layers
- Understanding the image layer cache
- Understand how CMD and ENTRYPOINT interact
- Difference between the COPY and ADD commands
- Using the VOLUME command inside a Dockerfile
- Run containers as non-root user
- Best practices for writing Dockerfiles
- Example: Build a Python application
- Use multi-stage builds
- Build secrets
- More best practices for writing Dockerfiles (Advanced) 
- Building Docker images from a container (Advanced)
- Building and Testing Multi-Arch Images (Advanced)
- Building Wasm Images (Advanced)
- Generate the SBOM for Docker images (Advanced)

### [Part 7: Sharing Docker Images](./Part_07_Sharing_Docker_Images/README.md)
- Working with registries, repositories, and image tags
- Create a repo on Docker Hub
- Pushing your own images to Docker Hub
- Run the image on a new instance
- Introducing self-hosted registries
- Running and using your own Docker registry
- Using image tags effectively
- Configure the credentials store (Advanced)

### [Part 8: Running Multi-container Apps With Docker Compose](./Part_08_Running_Multi_container_Apps_With_Docker_Compose/README.md)
- Overview of Docker Compose and installation
- Compose background
- Running a application with Compose: icta_app_minimal
- Development with Compose: icta_app_development
- Production deployment with Compose: icta_app_production
- Scaling and Load Balancing using Compose
- Advanced Compose features (Advanced)
- Example: Run ownCloud in Docker Compose

### [Part 9: Docker Reliability And Health Checks](./Part_09_Docker_Reliability_And_Health_Checks/README.md)
- Self-healing containers with restart policies
- Using restart policies in Docker Compose
- Understanding PID 1 in Docker containers
- Docker Resource Management (Advanced)
- Building health checks into Docker images
- Defining health checks and dependency checks in Docker Compose

### [Part 10: Managing Application Logs](./Part_10_Managing_Application_Logs/README.md)
- Docker logging overview
- Configure logging drivers

### [Part 11: Monitoring And Management](./Part_11_Monitoring_And_Management/README.md)
- Installing Portainer CE

### [Part 12: Docker Configuration Management](./Part_12_Docker_Configuration_Management/README.md)
- Secrets configuration in Docker Compose

### [Part 13: Docker Security](./Part_13_Docker_Security/README.md)
- Docker security overview
- Container security
- Container scanning

### [Part 14: Advanced Docker](./Part_14_Advanced_Docker/README.md)
- Run the Docker daemon as a non-root user - Rootless mode (Advanced)
- Podman

### [Part 15: Container orchestration and microservices](./Part_15_Container_orchestration_and_microservices/README.md)
- Traditional applications
- Microservices
- Moving from monolithic apps to microservices
- 12 Factor Apps
- Container Orchestration
- Kubernetes vs Docker Swarm

### [Part 16: Introduction to Kubernetes](./Part_16_Introduction_to_Kubernetes/README.md)
- About Kubernetes
- Kubernetes history
- Understanding Kubernetes
- The benefits of using Kubernetes
- Kubernetes architecture
- Kubernetes versions
- Install Kubernetes
- Should you even use Kubernetes?
- How Kubernetes runs an application
- Deploying your first application


## Changelog

The changelog is available [here](./CHANGELOG.md).

## Sources
- [Play with Docker Classroom](https://training.play-with-docker.com/)
