from django.db import models
from market.models import Product


class Address(models.Model):
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
    house_number = models.CharField(max_length=3, blank=True, null=True)
    corpus = models.CharField(max_length=2, blank=True, null=True)
    flat_number = models.CharField(max_length=4, blank=True, null=True)
    zip_code = models.CharField(max_length=6, blank=True, null=True)


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(max_length=20, default='', null=False)
    address = models.ManyToManyField(Address)


class Order(models.Model):
    order_date = models.DateField(auto_now=True)
    ship_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
