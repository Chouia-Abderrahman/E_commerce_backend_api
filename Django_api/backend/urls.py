from django.urls import path
from .views import create_product, read_product, category_list_create, edit_fetch_category
from rest_framework_simplejwt.views import TokenRefreshView
from .api.authentification.register import RegisterView
from .api.authentification.login import CustomTokenObtainPairView

urlpatterns = [
    path('products/', create_product, name='create_product'),
    path('categories/<int:id>', edit_fetch_category, name='edit_fetch_product'),
    path('categories/', category_list_create, name='categories'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]