from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=20)


class Category(models.TextChoices):
    HOODIE = "Hoodie"
    ACCESSORIES = "Accessories"
    PANTS = "Pants"


class Gender(models.TextChoices):
    MAN = 'M'
    WOMAN = 'F'
    NONE = 'N'


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    category = models.CharField(max_length=15, choices=Category.choices)
