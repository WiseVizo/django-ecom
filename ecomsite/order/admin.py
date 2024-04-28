from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', "get_user_name", 'get_user_email', 'get_user_shipping_address', 'get_cart_products') # Add the fields you want to display here
    
    def get_user_email(self, obj):
        return obj.cart.user.email
    get_user_email.short_description = 'User Email'  # Set the column header name

    def get_user_name(self, obj):
        return obj.cart.user.username
    get_user_name.short_description = "User's name"  # Set the column header name


    def get_user_shipping_address(self, obj):
        return obj.cart.user.shipping_address
    get_user_shipping_address.short_description = 'Shipping Address'  # Set the column header name


    def get_cart_products(self, obj):
        cart_items = obj.cart.cartitem_set.all()
        products = [f"{item.product.name} ({item.quantity})" for item in cart_items]
        return ', '.join(products)
    get_cart_products.short_description = 'Order Preview'




admin.site.register(Order, OrderAdmin)

