#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z db 5432; do
    sleep 0.5
    echo "Waiting for PostgreSQL to start."
done

echo "PostgreSQL started"

python3 /code/app.py