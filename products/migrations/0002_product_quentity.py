# Generated by Django 4.2.6 on 2024-02-06 09:18
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quentity",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
