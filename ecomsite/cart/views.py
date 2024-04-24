from django.shortcuts import render, redirect
from .models import Cart, CartItem
from product.models import Product
from django.contrib.auth.decorators import login_required
@login_required
def view_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = cart.cartitem_set.all()
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})
@login_required
def add_to_cart(request, product_id):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    product = Product.objects.get(id=product_id)
    CartItem.objects.create(cart=cart, product=product)
    return redirect('cart:view_cart')
@login_required
def remove_from_cart(request, cart_item_id):
    CartItem.objects.get(id=cart_item_id).delete()
    return redirect('cart:view_cart')