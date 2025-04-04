# Podman

- [Webpage](https://podman.io/)
- [Get Started with Podman](https://podman.io/get-started)
- [What is Podman?](https://docs.podman.io/en/latest/)
- [Tutorials](https://github.com/containers/podman/tree/main/docs/tutorials)

## About
Podman is a **daemonless, open source, Linux native tool designed to make it easy to find, run, build, share and deploy applications using Open Containers Initiative (OCI) Containers and Container Images**. 
- Podman provides a command line interface (CLI) familiar to anyone who has used the Docker Container Engine. 
- Most users can **simply alias Docker to Podman (alias docker=podman) without any problems**. 
Similar to other common Container Engines (Docker, CRI-O, containerd), Podman relies on an OCI compliant Container Runtime (runc, crun, runv, etc) to interface with the operating system and create the running containers. This makes the running containers created by Podman nearly indistinguishable from those created by any other common container engine.

## Frequently Asked Questions
- **Why is Podman more secure than Docker?**: Podman is more secure than Docker because of its daemon-less architecture, which makes it rootless. The rootless architecture of Podman allows users to work on their own containers or pods without interfering with other containers.

