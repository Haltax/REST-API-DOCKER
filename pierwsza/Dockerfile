# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
MAINTAINER JAKUBSTOPA

WORKDIR /app1-docker

COPY . .

RUN pip3 install -r requirements.txt
ENV FLASK_APP=pierwszy.py 

EXPOSE 5060

ENTRYPOINT ["python3", "pierwszy.py","-q","kolejka","-i","127.0.0.1"]
