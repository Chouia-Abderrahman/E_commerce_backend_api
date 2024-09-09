from django.db import models
from django.conf import settings
from .wishlist import Wishlist
from .product import Product

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
