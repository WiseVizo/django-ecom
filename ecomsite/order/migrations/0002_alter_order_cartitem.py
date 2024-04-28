# Generated by Django 5.0.4 on 2024-04-27 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="cartItem",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cart.cartitem"
            ),
        ),
    ]
