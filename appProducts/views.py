from django.http import HttpResponseRedirect
from django.shortcuts import render
from appProducts.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'appProducts/index.html', context)


def products(request, category_id=None, page=1):
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(product, per_page)
    products_paginator = paginator.page(page)

    context = {
        'title': 'Store - Каталог',
        'category': ProductCategory.objects.all(),
        'products': products_paginator,
    }
    return render(request, 'appProducts/products.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
