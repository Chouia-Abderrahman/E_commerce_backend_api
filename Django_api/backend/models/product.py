from django.db import models
from django.conf import settings
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    qty_stock = models.IntegerField(default=0, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
