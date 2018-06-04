from  celery import Celery

# CELERY_BROKER_URL = 'amqp://celery:celery@rabbitmq.service.sbay:5672/shanbay'
BROKER_URL = 'redis://localhost:6379/0'
app = Celery('tasks', broker=BROKER_URL)

@app.task
def add(x, y):
    return x + y