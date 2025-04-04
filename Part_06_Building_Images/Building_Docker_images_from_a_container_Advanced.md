# Building Docker images from a container (Advanced)

How do you produce a Docker image without a Dockerfile? The Dockerfile is there to automate the deployment of your app, but **you can’t always automate everything**. Sometimes you need to run the application and finish off some steps manually, and those steps can’t be scripted.

The basic workflow for building an image from a container includes three steps. 
1. First, you create a container from an existing image. You choose the image based on what you want to be included with the new finished image and the tools you need to make the changes.
2. The second step is to modify the filesystem of the container. These changes will be written to a new layer of the container’s union filesystem. We’ll revisit the relationship between images, layers, and repositories later in this chapter.
3. Once the changes have been made, the last step is to commit those changes. Then you’ll be able to create new containers from the resulting image.

With these steps in mind, work through the following commands to create a new image named `ubuntu-git`:
- Modifies file in container: `sudo docker container run -it -d --name ubuntu-git ubuntu:20.04 sleep 5000`
- `docker exec -it ubuntu-git /bin/bash`
- `apt update`
- `apt install git`
- `git --version`
- `exit`
- Commits change to new image: `sudo docker container commit ubuntu-git ubuntu-git`
- `sudo docker image ls`
- `sudo docker container rm -f ubuntu-git`
- Examines file in new container: `sudo docker container run --rm -it ubuntu-git /bin/bash`
- `git --version`
- `exit`
