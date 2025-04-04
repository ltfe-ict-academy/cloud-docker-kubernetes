# syntax=docker/dockerfile:1

# pull official base image
FROM python:3.11.9-slim-bookworm

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh
# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# install python dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN uv pip install --system --no-cache -r /usr/src/app/requirements.txt

# copy project
COPY . /usr/src/app
