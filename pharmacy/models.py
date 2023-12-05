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
    def __str__(self):
        return self.name
    
