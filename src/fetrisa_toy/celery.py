from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

# этот код скопирован с manage.py
# он установит модуль настроек по умолчанию Django для приложения 'celery'.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fetrisa_toy.settings")

# здесь вы меняете имя
app = Celery("fetrisa_toy")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object("django.conf:settings", namespace="CELERY")

# загрузка tasks.py в приложение django
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_newsletter": {
        "task": "main_store.tasks.send_newsletter",
        "schedule": crontab(minute="*/15"),  # Запуск каждые 15 минут
    },
}
