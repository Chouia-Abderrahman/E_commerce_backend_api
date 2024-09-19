
from rest_framework import generics
from ..models import WishlistItem
from ..serializers.wishlistitem import WishlistItemSerializer

class WishlistItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    lookup_field = 'id'

class WishlistItemListCreateView(generics.ListCreateAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    