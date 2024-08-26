FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./requirements.txt .

RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc libc-dev libffi-dev libssl-dev && \
  pip install --no-cache-dir -r requirements.txt && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

COPY . .
