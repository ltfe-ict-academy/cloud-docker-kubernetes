# syntax=docker/dockerfile:1

FROM python:3.11.9-slim-bookworm

RUN apt-get update && apt-get install -y procps netcat-traditional && rm -rf /var/lib/apt/lists/*
ADD . /code
WORKDIR /code
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
