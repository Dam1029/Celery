from __future__ import absolute_import
from celery import Celery

app = Celery('Celery',broker='redis://localhost',
                backend='redis://localhost',
                include=['Celery.tasks'])

app.config_from_object('Celery.config')

if __name__ == '__main__':
   app.start()