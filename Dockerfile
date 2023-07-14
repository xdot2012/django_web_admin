FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y

RUN apt-get -y install binutils libproj-dev gdal-bin
RUN apt-get -y install libjpeg-dev
RUN apt-get -y install zlib1g-dev
RUN apt-get -y install rabbitmq-server

RUN pip install --upgrade pip
RUN pip install ipython redis celery flower gunicorn

COPY ./code/requirements.txt /code/requirements.txt
WORKDIR code/
RUN pip install -r requirements.txt

COPY ./code .
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

EXPOSE 8000
CMD ["sh", "run-django.sh"]
