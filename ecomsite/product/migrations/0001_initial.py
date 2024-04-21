# Generated by Django 5.0.4 on 2024-04-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("category", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="product_images/")),
                ("stock_quantity", models.IntegerField(default=0)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("brand", models.CharField(max_length=50)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]