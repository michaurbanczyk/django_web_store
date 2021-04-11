from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(pk=order_id)
    subject = f"Zamownienie nr {order.id}"
    message = f"Witaj, {order.first_name}! Zlozyles zamowienie w naszym sklepie!." \
              f"Identyfikator zamowienia to {order.id}"
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent


@shared_task
def add(x,y):
    return x+y