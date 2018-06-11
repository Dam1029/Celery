from celery import Celery
from tasks import add

app = Celery('Celery',broker='redis://localhost',
                backend='redis://localhost',
                include=['Celery.tasks'])

app.config_from_object('Celery.config')

if __name__ == '__main__':
    app.start()
    # sum = add.delay(4,5)
    # print('sum is :', sum)
