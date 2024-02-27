from django.db import models
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    publish_date = models.DateField()
    
    def __str__(self):
        return self.title
