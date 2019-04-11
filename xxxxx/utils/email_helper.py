# coding: utf-8
from threading import Thread

from django.core.mail import send_mail
from django.conf import settings

from_email = settings.EMAIL_HOST_USER


def send_register_email(address, content):
    send_mail('xxxxx网站', content, from_email, [address], fail_silently=True)


def async_send_mail(address, content):
    Thread(target=send_register_email,args=(address, content)).start()
