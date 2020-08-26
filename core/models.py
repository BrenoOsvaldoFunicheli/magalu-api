# django formaters
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SendRequest(models.Model):
    TYPE_MESSAGE = (
        ('SMS','sms'),
        ('WTA','whatsapp'),
        ('PSH','push'),
        ('EML','e-mail')
    )

    sender = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    recipient = models.CharField(max_length=200)
    scheduled_time = models.DateTimeField(auto_now_add=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True, blank=True)
    type_message = models.CharField(max_length=3,choices=TYPE_MESSAGE)
    msg = models.TextField()
