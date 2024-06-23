from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('<int:product_id>/add_rating/', views.add_rating, name='add_rating'),
    path('rating/<int:rating_id>/edit/', views.edit_rating, name='edit_rating'),
]