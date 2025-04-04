# Building and Testing Multi-Arch Images (Advanced)

## Sources
- [Multi-platform images](https://docs.docker.com/build/building/multi-platform/)
- https://medium.com/@nshankar_88597/building-and-testing-multi-arch-images-with-docker-buildx-and-qemu-8f72c2f8728b
- https://cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm#:~:text=What%20is%20a%20multi%2Darch%20image%3F,-A%20multi%2Darch%20image
- Multi-architecture images (NP - 67)


## Overview
Docker images can support multiple platforms, which means that a single image may contain variants for different architectures, and sometimes for different operating systems, such as Windows.

When you run an image with multi-platform support, Docker automatically selects the image that matches your OS and architecture.

Most of the Docker Official Images on Docker Hub provide a variety of architectures. For example, the busybox image supports `amd64`, `arm32v5`, `arm32v6`, `arm32v7`, `arm64v8`, `i386`, `ppc64le`, and `s390x`. When running this image on an `x86_64` / `amd64` machine, the `amd64` variant is pulled and run.

## Building multi-platform images
When you invoke a build, you can set the `--platform` flag to specify the target platform for the build output. For example, `linux/amd64`, `linux/arm64`, or `darwin/amd64`.

By default, you can only build for a single platform at a time.

You can build multi-platform images using three different strategies, depending on your use case:
- Using the QEMU emulation support in the kernel
- Building on a single builder backed by multiple nodes of different architectures.
- Using a stage in your Dockerfile to cross-compile to different architectures