from django.shortcuts import redirect, render
from .models import Cart, Order

def order_now(request):
    if request.method == 'POST':
        # Assuming the user is authenticated and their cart is stored in the session
        user_cart = request.session.get('cart')
        print(f"user cart: {user_cart}")
        print(f"session: {request.session.items()}")
    
    return render(request, 'cart/cart.html')
