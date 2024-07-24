from django.urls import path
from .views import create_product, read_product

urlpatterns = [
    path('products/', create_product, name='create_product'),
    path('products/', read_product, name='read_product'),
]