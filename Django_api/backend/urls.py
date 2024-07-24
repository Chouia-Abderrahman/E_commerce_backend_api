from django.urls import path
from .views import create_product, read_product, category_list_create

urlpatterns = [
    path('products/', create_product, name='create_product'),
    path('categories/', category_list_create, name='categories'),
]