from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.PositiveIntegerField()

    def __str__(self):
        return self.name;