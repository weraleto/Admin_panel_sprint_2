#!/bin/sh

gunicorn --bind 0.0.0.0:8000 movies_admin.wsgi