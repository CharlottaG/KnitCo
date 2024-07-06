from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('our_story/', views.our_story, name='our_story'),
    path('return_policy/', views.return_policy, name='return_policy'),
    path('sustainability', views.sustainability, name='sustainability'),
    path('cookie_policy', views.cookie_policy, name='cookie_policy'),


]