from django.db import models


class Payment(models.Model):
    amount = models.FloatField()
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)