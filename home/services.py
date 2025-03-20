from django.core.mail import EmailMessage
import os


def create_reserve_table_message(user_data: dict):
    message = f"""
Table Reservation Details:
----------------------------
Client Name: {user_data.get("name")}
Client Email: {user_data.get("email")}
Number of People: {user_data.get("person")}
Arrival Time: {user_data.get("timing")}
Arrival Date: {user_data.get("date")}
"""
    if phone := user_data.get("phone"):
        message += "Client Phone Number: " + phone
    return message


def create_client_feedback_message(user_data: dict):
    message = f"""
Client Feedback:
----------------------------
Client Name: {user_data.get("name")}
Client Email: {user_data.get("email")}
Subject: {user_data.get("subject")}
Client Phone Number: {user_data.get("phone")}
Message: {user_data.get("message")}
"""
    return message


def send_email(subject: str, message: str) -> None:
    admin_email = os.environ.get("email")
    email = EmailMessage(subject, message, to=[admin_email])  # pyright:ignore
    email.send()
