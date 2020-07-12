# A Simple Django Stack

A clean, organized stack for django development.

1. Added a simple authentication app<br>
2. Added Celery/RabbitMQ/Flower

# Development

run server<br>
```
python manage.py runserver
```

RabbitMQ on docker<br>
```
sudo docker run -d -p 5672:5672 rabbitmq
```

Celery<br>
```
celery -A meuapp worker -l info
```

Flower<br>
```
celery -A meuapp flower
```
