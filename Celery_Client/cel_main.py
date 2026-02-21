from celery import Celery
import time
import smtplib
from email.message import EmailMessage
# app = Celery("cel_main", broker="pyamqp://")
app = Celery("cel_main", broker="pyamqp://localhost//")


@app.task
def TaskQueue(message):
    time.sleep(10)
    print("TaskQueue: {0}".format(message))


@app.task
def write_log(logs):
    print("Writing logs: {0}".format(logs))



SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
_count = 0

@app.task(bind=True, max_retries=3)
def email_send(self, recipient_email):
    # try:
    #     msg = EmailMessage()
    #     msg["Subject"] = "Background Email"
    #     msg["From"] = SENDER_EMAIL
    #     msg["To"] = recipient_email
    #     msg.set_content("Hello! This email was sent using Celery.")

    #     with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    #         server.starttls()
    #         server.login(SENDER_EMAIL, SENDER_PASSWORD)
    #         server.send_message(msg)

    #     print(f"Email sent to {recipient_email}")

    # except Exception as exc:
    #     raise self.retry(exc=exc, countdown=60)
    global _count
    _count += 1.5
    time.sleep(_count)
