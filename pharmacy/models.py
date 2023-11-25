from django.db import models
import pharmacy
from products.models import Product


class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pharmacy_images/', null=True, blank=True)
    open_time = models.TimeField(default='00:00:00')
    close_time = models.TimeField(default='00:00:00')
    phone = models.CharField(max_length=20)
    prodcuts=models.ManyToManyField(Product,blank=True) 
    def __str__(self):
        return self.name
    
class ProductItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(help_text='Quantity of the product')
    prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE)


class Prescription(models.Model):
    patient = models.ForeignKey('accounts.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.IntegerField()
    pharmacy = models.ForeignKey('pharmacy.Pharmacy', on_delete=models.SET_NULL, null=True, blank=True)