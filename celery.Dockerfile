FROM python:3

ENV DEBIAN_FRONTEND=noninteractive
COPY . /docxtopdf
COPY requirements.txt /docxtopdf/docxtopdf
WORKDIR /docxtopdf/docxtopdf
RUN apt update -qq && apt install -y default-jre libreoffice-writer  && pip3 install -r requirements.txt






ENTRYPOINT ["celery","-A", "docxtopdf", "worker", "-l", "INFO"]
