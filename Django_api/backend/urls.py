from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .api.authentification.register import RegisterView
from .api.authentification.login import CustomTokenObtainPairView
from .api.cart_api import CartListCreateView, CartRetrieveUpdateDestroyAPIView
from .api.cartitem_api import CartItemListCreateView, CartItemRetrieveUpdateDestroyAPIView
from .api.category_api import CategoryListCreateView, CategoryRetrieveUpdateDestroyAPIView
from .api.order_api import OrderListCreateView, OrderRetrieveUpdateDestroyAPIView
from .api.orderitem_api import OrderItemListCreateView, OrderItemRetrieveUpdateDestroyAPIView
from .api.payment_api import PaymentListCreateView, PaymentRetrieveUpdateDestroyAPIView
from .api.product_api import ProductListCreateView, ProductRetrieveUpdateDestroyAPIView, products_by_category
from .api.profile_api import ProfileListCreateView, ProfileRetrieveUpdateDestroyAPIView
from .api.review_api import ReviewListCreateView, ReviewRetrieveUpdateDestroyAPIView
from .api.wishlist_api import WishlistListCreateView, WishlistRetrieveUpdateDestroyAPIView
from .api.wishlistitem_api import WishlistItemListCreateView, WishlistItemRetrieveUpdateDestroyAPIView
from .views import check_login
from .api.swagger import schema_view


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:id>/', CartRetrieveUpdateDestroyAPIView.as_view(), name='cart-retrieve-update-delete'),

    path('cartitems/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('cartitems/<int:id>/', CartItemRetrieveUpdateDestroyAPIView.as_view(), name='cartitem-retrieve-update-delete'),

    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-delete'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:id>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update-delete'),

    path('orderitems/', OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('orderitems/<int:id>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='orderitem-retrieve-update-delete'),

    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:id>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-retrieve-update-delete'),
    path('products/category/<int:categoryId>/', products_by_category, name='products-by-category'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-delete'),

    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:id>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-retrieve-update-delete'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:id>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-retrieve-update-delete'),

    path('wishlists/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlists/<int:id>/', WishlistRetrieveUpdateDestroyAPIView.as_view(), name='wishlist-retrieve-update-delete'),

    path('wishlistitems/', WishlistItemListCreateView.as_view(), name='wishlistitem-list-create'),
    path('wishlistitems/<int:id>/', WishlistItemRetrieveUpdateDestroyAPIView.as_view(), name='wishlistitem-retrieve-update-delete'),

    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('check-login/', check_login, name='check_login'),
]