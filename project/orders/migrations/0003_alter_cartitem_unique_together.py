# Generated by Django 4.2.6 on 2024-06-27 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
        ("orders", "0002_order_location_order_owner_order_phone"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="cartitem",
            unique_together={("cart", "product")},
        ),
    ]