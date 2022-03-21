FROM python:3

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . /docxtopdf
WORKDIR /docxtopdf/docxtopdf

COPY requirements.txt /docxtopdf/docxtopdf
RUN  pip3 install -r requirements.txt  






