
from django.urls import path
from appProducts.views import products

app_name = 'appProducts'

urlpatterns = [
    path('', products, name='products'),
]

