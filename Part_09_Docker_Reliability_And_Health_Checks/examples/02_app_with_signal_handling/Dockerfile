# syntax=docker/dockerfile:1

FROM python:3.11.9-slim-bookworm

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

ADD . /code
WORKDIR /code
ENTRYPOINT ["python", "-u", "app.py"]
