# DOCKER

# Docker to narzędzie pozwalające na uruchamianie aplikacji w izolowanych środowiskach nazywanych kontenerami.
# Kontenery zawierają wszystkie potrzebne zależności do uruchomienia aplikacji, co zapewnia spójność działania na 
# różnych środowiskach.
'''''''''
Zalety Dockera:
    izolacja środowiska
    łatwkę wdrążenie w aplikacje, projekty, łatwe skalowanie
    łatwa dystrybujca aplikacji

https://docs.docker.com/get-started/get-docker/

docker --version
docker info

docker pull <nazwa_obraz> - pobieranie obrazu
docker run <nazwa_obrazu_ lub id_obrazu>    

docker ps - wyświetla uruchomione kontynery 
docker start <id_kontenera> - uruchomienie kontenera
docker stop <id_kontenera> - zatrzymanie kontenera

docker images - wyświetlenie dostępnych obrazów 

https://hub.docker.com/repositories/zaxqua

redis


DockerFile:
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]

docker build -t my_app . 
docker image
docker rmi image_id 

docker run -d -p 5000:5000 my_app

docker_compose.yml:

version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis
  redis:
    image: redis:alpine


docker run -d --name web ... 
docker run -d --name db ... 
docker run -d --name redis ...

docker compose up -d
dcoker compose down

'''


