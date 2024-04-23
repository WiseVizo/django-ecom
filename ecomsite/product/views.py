from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 3  # Number of products per page
        
    def post(self, request, *args, **kwargs):
        # Handle POST request for search form submission
        query = self.request.POST.get('search')
        if query:
            products = Product.objects.filter(name__icontains=query)
        else:
            products = Product.objects.all()
        return render(request, self.template_name, {'products': products})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html' 
    context_object_name = 'product' 
