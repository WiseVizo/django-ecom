from django.shortcuts import render, redirect
from .models import Cart, CartItem
from product.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = cart.cartitem_set.all()
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})
@login_required
def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    
    # Check if the product is already in the cart
    cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # If the cart item is newly created, set its quantity to 1
    if cart_item_created:
        cart_item.quantity = 1
        cart_item.save()
        messages.success(request, f'{product.name} added to your cart.')
    else:
        # If the cart item already exists, increment its quantity by 1
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'{product.name} quantity updated in your cart.')

    return redirect('cart:view_cart')
@login_required
def remove_from_cart(request, cart_item_id):
    CartItem.objects.get(id=cart_item_id).delete()
    return redirect('cart:view_cart')