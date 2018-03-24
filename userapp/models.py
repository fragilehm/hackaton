from django.db import models


# Create your models here.


class User(models.Model):
    """Модель юзера"""
    status_type = (("USER", "user"),
                    ("ORGANIZATION", "organization"))
    type = models.CharField(max_length=40, choices=status_type, default="USER")
    phone = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    connectedTo = models.ManyToManyField('self', blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.phone)

    class Meta:
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"


class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
