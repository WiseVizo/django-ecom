from django.db import models
from cart.models import Cart


# Define your Order model
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


    def __str__(self) -> str:
        user_name = self.cart.user.username
        return f"Order for {user_name}"
