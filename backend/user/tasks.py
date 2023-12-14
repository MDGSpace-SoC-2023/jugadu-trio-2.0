from celery import shared_task
from django.core.mail import send_mail
import secrets

@shared_task
def send_email_func(subject,sender, receiver):
    numeric_otp =  ''.join(secrets.choice('0123456789') for _ in range(6))
    message = f"Your otp is {numeric_otp}"
    send_mail(subject, message, sender, [receiver])