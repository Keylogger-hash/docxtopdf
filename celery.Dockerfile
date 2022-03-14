FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir app/ && apt update -qq && apt -y install python3 python3-dev python3-pip libreoffice libpq-dev

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt




VOLUME [ "/app" ]
RUN ls -a
ENTRYPOINT ["celery","-A", "docxtopdf", "worker", "-l", "INFO"]