from django.db import models

# Create your models here.
# 1 when we have started to make admin panel
class Customer(models.Model):
    name = models.CharField(max_length = 300, null=True)
    phone = models.CharField(max_length = 300, null=True)
    email = models.CharField(max_length = 300, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def _str_(self):
        return self.name
class Product(models.Model):
    CATEGORY = (
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )


    name = models.CharField(max_length = 300, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length = 300, null=True,choices=CATEGORY)
    description = models.CharField(max_length = 300, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('delivered','delivered'),
    )

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=300, null=True, choices=STATUS)
