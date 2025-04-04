# Managing Application Logs

## Sources
- [Docker: Configure logging drivers](https://docs.docker.com/config/containers/logging/configure/)
- [Docker Logging: A Complete Guide](https://sematext.com/guides/docker-logs/)

## Docker logging overview

The `docker logs` command shows information logged by a running container. The information that's logged and the format of the log depends almost entirely on the container's endpoint command.

By default, docker logs shows the command's output just as it would appear if you ran the command interactively in a terminal. Unix and Linux commands typically open three I/O streams when they run, called STDIN, STDOUT, and STDERR. 
- **STDIN** is the command's input stream, which may include input from the keyboard or input from another command. 
- **STDOUT** is usually a command's normal output.
- **STDERR** is typically used to output error messages. 

By default, docker logs shows the command's STDOUT and STDERR. 

In some cases, docker logs may not show useful information unless you take additional steps:
- If you use a logging driver which sends logs to a file, an external host, a database, or another logging back-end, and have "dual logging" disabled, docker logs may not show useful information.
- If your image runs a non-interactive process such as a web server or a database, that application may send its output to log files instead of STDOUT and STDERR.


## Configure logging drivers
Docker includes multiple logging mechanisms to help you get information from running containers and services. These mechanisms are called logging drivers. Each Docker daemon has a default logging driver, which each container uses unless you configure it to use a different logging driver, or log driver for short.

**As a default, Docker uses the `json-file` logging driver, which caches container logs as JSON internally.** In addition to using the logging drivers included with Docker, you can also implement and use logging driver plugins.

> ❗❗ **By default, no log-rotation is performed.** As a result, log-files stored by the default json-file logging driver logging driver can cause a significant amount of disk space to be used for containers that generate much output, which can lead to disk space exhaustion. Docker keeps the json-file logging driver (without log-rotation) as a default to remain backward compatibility with older versions of Docker, and for situations where Docker is used as runtime for Kubernetes. For other situations, the **local logging driver is recommended** as it performs log-rotation by default, and uses a more efficient file format.
