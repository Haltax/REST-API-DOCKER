# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app3-docker

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5060

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]                            
