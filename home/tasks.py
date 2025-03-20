from core.celery import app
import os
from .services import send_email


@app.task
def send_email_for_reservation(message: str) -> None:
    send_email("Client Feedback", message)


@app.task
def send_client_feedback(message: str) -> None:
    send_email("Client Feedback", message)
