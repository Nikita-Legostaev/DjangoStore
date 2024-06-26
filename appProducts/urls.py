from django.urls import path
from appProducts.views import products, basket_add,basket_remove

app_name = 'appProducts'

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page>', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:id>/', basket_remove, name='basket_remove'),
]
