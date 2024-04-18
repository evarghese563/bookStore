from django.db import models

# Create your models here.


class Manga(models.Model):
    name = models.CharField(max_length = 256)
    price = models.FloatField()
    quantity = models.FloatField()
<<<<<<< HEAD
    image_url = models.URLField(default='/static/8cbad94afb0bd6bd235cdc917a9c7f83.jpg')


    def __str__(self):
        return self.name


=======
>>>>>>> upstream/main
