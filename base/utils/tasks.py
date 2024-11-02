from celery import shared_task
from .email_service import EmailService

@shared_task
def send_email_task(to, subject, text_body, html_body):
    email_service = EmailService()
    email_service.send_email(to, subject, text_body, html_body)
