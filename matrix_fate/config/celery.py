from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Устанавливаем настройки для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаем объект Celery
app = Celery('config')

# Загружаем настройки Celery из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи, определенные в приложениях Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# celery -A config worker --loglevel=info
