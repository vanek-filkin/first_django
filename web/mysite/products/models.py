from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    type_of = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    rel_date = models.DateTimeField()
