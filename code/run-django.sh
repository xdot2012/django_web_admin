#!/bin/sh

cd /code
sleep 10;


echo "Migrate Databases..."
python manage.py migrate

echo "Starting Server..."
gunicorn meuapp.wsgi:application --limit-request-line 0 --worker-tmp-dir /dev/shm --preload --config gunicorn_hooks.py --timeout 900 -w 17 -b :8000