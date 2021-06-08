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
    img = models.ImageField(upload_to='images/' )

    def __str__(self):
        result = (self.name + '\n' + self.type_of + self. manufacturer + '\n' +
        self.country + '\n' + self.description + '\n' + str(self.price) + '\n' +
        str(self.rel_date.year))

        return result

    def was_release_recently(self):
        return self.rel_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        ordering = ['-rel_date', '-price']