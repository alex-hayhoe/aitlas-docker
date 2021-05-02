# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get install nvidia-container-runtime
RUN docker run -it --rm --gpus all ubuntu nvidia-smi
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
