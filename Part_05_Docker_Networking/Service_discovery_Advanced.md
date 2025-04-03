# Service discovery (Advanced)

As well as core networking, libnetwork also provides some important network services.

Service discovery allows all containers and Swarm services to locate each other by name. The only requirement is that they be on the same network.

Under the hood, this leverages Docher’s embedded DNS server and the DNS resolver in each container.
<!-- 

- NP - 169
- https://docs.docker.com/config/containers/container-networking/#dns-services -->
