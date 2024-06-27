from django.db import models
from libraries.models import Library

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Copy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.book.title} - Copy {self.copy_number}"
