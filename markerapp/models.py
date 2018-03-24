from django.db import models
from userapp.models import User

# Create your models here.


class Category(models.Model):
    """Модель категории"""
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Marker(models.Model):
    """Модель маркера"""
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    address = models.CharField(max_length=150)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    isNeed = models.BooleanField()

    user_id = models.IntegerField()
    user_phone = models.CharField(max_length=50)
    user_email = models.EmailField(null=True, blank=True)
    user_name = models.CharField(null=True, blank=True, max_length=50)
    user_surname = models.CharField(null=True, blank=True, max_length=50)
    user_description = models.TextField(null=True, blank=True)
    user_image = models.URLField(null=True, blank=True)
    user_connectedTo = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}".format(self.description)

    class Meta:
        verbose_name = "Маркер"
        verbose_name_plural = "Маркеры"

