# A Simple Django Stack

A clean, organized stack for django development.

1. Added a simple authentication app<br>
2. Added Celery/RabbitMQ/Flower
3. Added Django Celery Beat periodic tasks
4.

# To do
Add Docker

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

Task Scheduler<br>
You can enter django admin panel and register periodic tasks.
```
celery -A proj beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
