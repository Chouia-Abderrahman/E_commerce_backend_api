from django.contrib.auth.models import User
from django.db import models

class Wishlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    qty_stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Payment(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    total_amount = models.FloatField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
