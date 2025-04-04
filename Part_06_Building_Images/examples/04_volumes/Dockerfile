# syntax=docker/dockerfile:1

FROM ubuntu:20.04

WORKDIR /data
RUN echo "Hello from Volume" > test

RUN mkdir /uploads

VOLUME /data
VOLUME /uploads

CMD ["sleep", "10000"]
