from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('', include('login.urls')),
    path('login/', include('login.urls')),
    path('servicos/', include('servicos.urls')),
]
