from django.conf import settings
from django.core.mail import send_mail

from fetrisa_toy.celery import app
from main_store.models import User


@app.task
def send_newsletter():
    email_list = User.objects.values_list("email", flat=True)

    # Отправка письма со ссылкой на сброс пароля
    subject = "Рассылка"
    message = f"Не забывайте про нас, новые игрушки уже ждут вас"
    for email in email_list:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
