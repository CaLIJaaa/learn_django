from django.shortcuts import render, HttpResponse
from products.models import ProductCategory


def index(request):
    return render(request, 'products/index.html')


def products(request):
    product = {'products': ProductCategory.objects.all()}
    return render(request, 'products/products.html', product)