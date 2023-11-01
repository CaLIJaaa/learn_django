from django.shortcuts import render, HttpResponse
from products.models import ProductCategory, Product


def index(request):
    return render(request, 'products/index.html')


def products(request):
    product = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', product)