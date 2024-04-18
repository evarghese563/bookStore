from django.db import models

# Create your models here.


class Manga(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)  # Making image_url optional

    def __str__(self):
        return self.name
