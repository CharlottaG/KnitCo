from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/add_rating/', views.add_rating, name='add_rating'),
    path('rating/<int:rating_id>/edit/', views.edit_rating, name='edit_rating'),
    path('rating/<int:rating_id>/delete/', views.delete_rating, name='delete_rating'),
    path('add', views.add_product, name='add_product'),
     path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]