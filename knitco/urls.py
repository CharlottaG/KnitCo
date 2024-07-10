from django.contrib import admin
from django.urls import path, include
from .views import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('account/', include('allauth.urls')),
    path('', include('home.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('products/', include('products.urls')),
    path('profiles/', include('profiles.urls')),
]

# Custom 404 handler
handler404 = 'knitco.views.handler404'
