from django.db import models

# Create your models here.


class Manga(models.Model):
    name = models.CharField(max_length = 256)
    price = models.FloatField()
    quantity = models.FloatField()
