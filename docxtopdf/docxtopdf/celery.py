from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docxtopdf.settings')
app = Celery('docxtopdf')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug(self):
    return True
