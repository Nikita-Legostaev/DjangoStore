from django.contrib import admin

from appProducts.models import Product, ProductCategory, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'category')
    fields = ('name', 'quantity', 'price', 'category', 'description', 'image')
    search_fields = ('name', 'description')
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
