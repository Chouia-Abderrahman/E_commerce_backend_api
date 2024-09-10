from django.urls import path
from .views import create_product, read_product
from rest_framework_simplejwt.views import TokenRefreshView
from .api.authentification.register import RegisterView
from .api.authentification.login import CustomTokenObtainPairView
from .api.category.category_edit_fetch_delete import CategoryRetrieveUpdateDestroyView
from .api.category.category_list_create import CategoryListCreateView
from .api.product.product_list_create import ProductListCreateView
from .api.product.product_edit_fetch_delete import ProductRetrieveUpdateDestroyAPIView
from .api.product.product_fetch_by_category import products_by_category
from .api.payment.payment_list_create import PaymentListCreateView
from .api.payment.payment_edit_fetch_delete import PaymentRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-edit-fetch'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update'),
    path('products/category/<int:categoryId>/', products_by_category, name='products-by-category'),

    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:id>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-retrieve-update-delete'),

    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
