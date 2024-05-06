from django.contrib import admin
from users.models import User
from appProducts.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    inlines = (BasketAdmin,)
