# syntax=docker/dockerfile:1

FROM node:20-alpine

ENV TARGET="ltfe.org"
ENV METHOD="HEAD"
ENV INTERVAL="3000"

WORKDIR /web-ping
COPY app.js .

CMD ["node", "/web-ping/app.js"]
