FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir app/ && apt update -qq && apt -y install postgresql postgresql-contrib python3 python3-dev python3-pip libpq-dev 

COPY . /app
WORKDIR /app
VOLUME [ "/app" ]
RUN pip3 install -r requirements.txt && python3 manage.py makemigrations && python3 manage.py migrate





RUN ls -a

ENTRYPOINT ["gunicorn", "docxtopdf.wsgi","--bind 0.0.0.0:8000","--access-logfile","INFO"]
