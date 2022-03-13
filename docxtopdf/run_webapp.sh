#!/bin/sh

#cd docxtopdf

python3 manage.py makemigrations

python3 manage.py migrate

gunicorn docxtopdf.wsgi --bind 0.0.0.0:8000 --access-logfile INFO