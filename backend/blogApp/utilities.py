from django.core.mail import send_mail
from django.template.loader import render_to_string
from . import models


def send_new_post_notification(post):
    """Отправка уведомлений о новом посте на почту"""
    host = f'http://localhost:8080/{post.slug}'
    context = {
        'title': post.title,
        'category': post.category,
        'host': host,
    }
    subscribers_queryset = models.Contact.objects.all()
    subscribers = [subscriber.email for subscriber in subscribers_queryset]
    subject = render_to_string('email/new_post_letter_subject.txt')
    html_body = render_to_string('email/new_post_letter_body.html', context)
    send_mail(subject, html_body, 'oskolok2013@gmail.com', subscribers, html_message=html_body)


def get_client_ip(request):
    """Получени ip клиента"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
