from django.db import models
from django.conf import settings
from .payment import Payment

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    total_amount = models.FloatField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)