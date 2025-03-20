from django.core.mail import EmailMessage
from core.celery import app
import os


@app.task
def send_email_for_reservation(message):
    admin_email = os.environ.get("email")
    email = EmailMessage(
        "Table Reservation", message, to=[admin_email]  # pyright:ignore
    )
    email.send()
