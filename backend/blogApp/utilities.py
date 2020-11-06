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
    subscribers_queryset= models.Contact.objects.all()
    subscribers = [subscriber.email for subscriber in subscribers_queryset]
    subject = render_to_string('email/new_post_letter_subject.txt')
    body = render_to_string('email/new_post_letter_body.txt', context)
    send_mail(subject, body, 'oskolok2013@gmail.com', subscribers)

