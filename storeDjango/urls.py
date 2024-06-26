
from django.contrib import admin
from django.urls import path, include
from appProducts.views import index
from django.conf.urls.static import static
from django.conf import settings
from users.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('appProducts.urls', namespace='products')),
    path('userss/', include('users.urls', namespace='users')),
    path('login/', login, name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
