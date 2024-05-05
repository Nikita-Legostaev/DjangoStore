from django.shortcuts import render, HttpResponse
from appProducts.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'appProducts/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all(),
    }
    return render(request, 'appProducts/products.html', context)
