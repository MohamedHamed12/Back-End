# Generated by Django 4.2.6 on 2024-03-23 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_paymoborder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymoborder',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]