from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    brand = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    is_available = models.BooleanField()

class Review(models.Model):
    reviewed_by = models.CharField(max_length=255)
    reviwed_on = models.DateTimeField()
    text = models.TextField()