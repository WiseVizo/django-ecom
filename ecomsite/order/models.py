from django.db import models
from cart.models import CartItem, Cart


# Define your Order model
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


    def __str__(self) -> str:
        user_email = self.cart.user.email
        return f"Order for {user_email}"
