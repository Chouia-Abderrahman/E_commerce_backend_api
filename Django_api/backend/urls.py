from django.urls import path
from .views import create_product, read_product, category_list_create, edit_fetch_category

urlpatterns = [
    path('products/', create_product, name='create_product'),
    path('categories/<int:id>', edit_fetch_category, name='edit_fetch_product'),
    path('categories/', category_list_create, name='categories'),
]