#!/bin/bash

set -e

echo 'running migrations'

python kanairo/manage.py migrate --noinput
gunicorn --chdir kanairo kanairo.wsgi --bind 0.0.0.0:8000 
