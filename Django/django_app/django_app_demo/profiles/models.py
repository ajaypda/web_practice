from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=10)
    country = models.CharField(max_length=255)

class Message(models.Model):
    sender_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    text = models.TextField()
    is_deleted = models.BooleanField()
    sent_on = models.DateTimeField()