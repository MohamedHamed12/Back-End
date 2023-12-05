from django.db import models

# Create your models here.



class Order(models.Model):
    patient = models.ForeignKey('accounts.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.IntegerField()
    pharmacy = models.ForeignKey('pharmacy.Pharmacy', on_delete=models.SET_NULL, null=True, blank=True)