from django.shortcuts import redirect, render
from .models import  Order
from django.contrib.auth import get_user_model
from cart.models import CartItem


User = get_user_model()

def order_now(request):
    if request.method == 'POST':
        # Assuming the user is authenticated and their cart is stored in the session
        user_id = request.session['_auth_user_id']
        print(f"user id: {user_id}")
        user = User.objects.get(pk=user_id)
        print(f"user : {user}")
        user_cart = user.cart_set.all()[0]
        print(f"user cart: {user_cart}")
        order = Order.objects.create(cart=user_cart)
        # CartItem.objects.filter(cart=user_cart).delete() # create order item caz products in oder are cartitem and if we remove cartitem products in order will also get removed 
    return render(request, 'order/order.html', {"cart": user_cart})
