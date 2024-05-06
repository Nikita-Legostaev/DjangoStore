from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from appProducts.models import Product, ProductCategory, Basket
from users.models import User


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


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
