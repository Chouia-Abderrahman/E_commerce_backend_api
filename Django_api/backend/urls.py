from django.urls import path
from .views import create_product, read_product
from rest_framework_simplejwt.views import TokenRefreshView
from .api.authentification.register import RegisterView
from .api.authentification.login import CustomTokenObtainPairView
from .api.category.category_edit_fetch_delete import CategoryRetrieveUpdateDestroyView
from .api.category.category_list_create import CategoryListCreateView
from .api.product.product_list_create import ProductListCreateView
from .api.product.product_edit_fetch_delete import RetrieveUpdateDestroyAPIView

urlpatterns = [

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:id>/', RetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update'),

    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-edit-fetch'),

    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]