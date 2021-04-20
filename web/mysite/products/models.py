from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    type_of = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    rel_date = models.DateTimeField()
    def __str__(self):
        return self.name;
    def was_release_recently(self):
        return self.rel_date >= timezone.now() - datetime.timedelta(days=1)