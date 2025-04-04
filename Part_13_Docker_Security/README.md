# Docker Security

## Sources
- [Security](https://docs.docker.com/security/)
- [Docker security](https://docs.docker.com/engine/security/)
- [5 Developer Workstation Security Best Practices](https://www.docker.com/blog/developer-workstation-security-best-practices/)
- [What is the Best Container Security Workflow for Your Organization?](https://www.docker.com/blog/what-is-the-best-container-security-workflow/)
- [What is container security?](https://snyk.io/learn/container-security/)


## Docker security overview
There are four major areas to consider when reviewing Docker security:
- The intrinsic security of the kernel and its support for namespaces and cgroups
- The attack surface of the Docker daemon itself
- Loopholes in the container configuration profile, either by default, or when customized by users.
- The "hardening" security features of the kernel and how they interact with containers.

## Container security
Vulnerabilities can be introduced to containers in a number of ways: 
- from the software inside the container, 
- how the container interacts with the host operating system and adjacent containers, 
- the configurations for networking and storage
- from other images that your containers rely on
    - your container image may be based on a publicly available image that contains known vulnerabilities and malware, especially if you didn’t download the image from a verified publisher and authenticate the image publisher and contents

## Container scanning

Container scanning, or container image scanning, is the process and scanning tools used to identify vulnerabilities within containers and their components. It’s key to container security, and enables developers and cybersecurity teams to fix security threats in containerized applications before deployment.

**A container scanner is an automated tool that analyzes these various container components to detect security vulnerabilities.**

Security scanners can be **integrated during various stages of development**:
- scan potential parent images from your desktop before deciding which one to use as the base for your image
- using IDE plugins
- integrate container vulnerability scanning into the continuous integration and continuous delivery (CI/CD)
- monitor containerized deployments when they’re running on Kubernetes or another platform
- scanning container registries is also a great way to reduce the number of vulnerabilities across all of the frequently used images in your organization
    - You can also monitor your stored images over time, to identify any newly disclosed vulnerabilities in your existing images and prevent those from being deployed to production in the future.

Most container scanning solutions leverage a public source for vulnerability information like the National Vulnerability Database (NVD) or the Common Vulnerabilities & Exposures (CVE) database. These databases publish known exploits to enable automated vulnerability management, security measurement, and compliance. 

Each new layer has the risk of introducing new vulnerabilities into the container, so it’s crucial that the container scanner you use can detect issues layer by layer.

> **How does Container scanning work?** Scanning containers for vulnerabilities usually involves a security tool that analyzes a container image layer by layer to detect potential security issues. Most scanning solutions leverage a database of known vulnerabilities so that organizations can stay up-to-date as the security threat landscape evolves. Containerized applications also consist of multiple components, including custom code, open source dependencies, images, Dockerfiles, and more. Scanning for vulnerabilities across all of these components is critical for comprehensive container security.


<!-- - Understanding users
    - Working with the run-as user -->

<!-- ## Other
Containers and isolation features have existed for decades. Docker uses Linux namespaces
and cgroups, which have been part of Linux since 2007. 

Docker builds containers using 10 major system features. Part 1 of this book uses
Docker commands to illustrate how these features can be modified to suit the needs
of the contained software and to fit the environment where the container will run.
The specific features are as follows:
- PID namespace—Process identifiers and capabilities
- UTS namespace—Host and domain name
- MNT namespace—Filesystem access and structure
- IPC namespace—Process communication over shared memory
- NET namespace—Network access and structure
- USR namespace—User names and identifiers
- chroot syscall—Controls the location of the filesystem root
- cgroups—Resource protection
- CAP drop—Operating system feature restrictions
- Security modules—Mandatory access controls -->
