from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images', null=True, blank=True)

class Discount(models.Model):

    percentage = models.IntegerField(help_text='Percentage of discount')
    product = models.ForeignKey('Product', on_delete=models.CASCADE,help_text='Product for which the discount is applicable')
    start_date = models.DateField(null=True, blank=True, help_text='Start date of the discount')
    end_date = models.DateField(null=True, blank=True, help_text='End date of the discount')



class Product(models.Model):
    name = models.CharField(max_length=255, help_text='Name of the medication')
    generic_name = models.CharField(max_length=255, help_text='Generic name of the medication')
    form = models.CharField(max_length=255, help_text='Form of the medication (e.g., tablet, capsule, liquid)')
    strength = models.CharField(max_length=255, help_text='Strength of the medication (e.g., 500mg)')
    factory_company = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    orders = models.ManyToManyField('orders.Order', through='products.OrderItem', related_name='products')
    pharmacy = models.ForeignKey('pharmacy.Pharmacy', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(help_text='Quantity of the product')
    def __str__(self):
        return self.product.name