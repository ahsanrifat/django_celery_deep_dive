from celery import shared_task
from django.core.mail import send_mail
from celery_project import settings


@shared_task(bind=True)
def test_celery(self):
    import time

    time.sleep(3)
    for i in range(10):
        print(i)
    return "Done"


@shared_task(bind=True)
def send_email(self):
    emails = ["syed.rifat.ahsan@gmail.com", "rifat.mtb@gmail.com"]
    for email in emails:
        print(email)
        mail_subject = "Hi, Celery Testing"
        message = "This is test message for celery testing"
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
