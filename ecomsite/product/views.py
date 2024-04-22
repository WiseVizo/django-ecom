from django.views.generic import ListView
from .models import Product
from django.core.paginator import Paginator

class ProductListView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 3  # Number of products per page