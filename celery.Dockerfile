FROM python:3

ENV DEBIAN_FRONTEND=noninteractive
COPY . /app
WORKDIR /app
RUN apt update -qq && apt install -y default-jre libreoffice-java-common && pip3 install -r requirements.txt






VOLUME [ "/app" ]
#ENTRYPOINT ["celery","-A", "docxtopdf", "worker", "-l", "INFO"]
