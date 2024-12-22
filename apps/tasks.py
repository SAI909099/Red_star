from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_verification_email(email, verification_code):
    subject = "Verify Your Email"
    message = f"Your verification code is: {verification_code}"
    from_email = "no-reply@volumenzeit.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Verification email sent to {email}"
