#!/bin/sh

python manage.py migrate --no-input

python manage.py collectstatic --no-input

gunicorn --bind 0.0.0.0:80 movies_admin.wsgi