from django.core.mail import EmailMessage
from core.celery import app
import os


@app.task
def send_email_for_reservation(message: str) -> None:
    admin_email = os.environ.get("email")
    email = EmailMessage(
        "Table Reservation", message, to=[admin_email]  # pyright:ignore
    )
    email.send()


@app.task
def send_client_feedback(message: str) -> None:
    admin_email = os.environ.get("email")
    email = EmailMessage("Client Feedback", message, to=[admin_email])  # pyright:ignore
    email.send()
