from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1500)
    price = models.IntegerField()
    image = models.ImageField(upload_to="photos/%Y/%m/%d")

    def __str__(self) -> str:
        return self.name
