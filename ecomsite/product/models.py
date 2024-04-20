from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/', default='product_images/placeholder_product.webp')
    stock_quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name