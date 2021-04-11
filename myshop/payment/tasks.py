from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order


@shared_task
def payment_completed(order_id):
    order = Order.objects.get(pk=order_id)
    subject = f"Zamownienie nr {order.id}"
    message = f"Zaplacono!."
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
