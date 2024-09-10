from rest_framework import serializers
from ..models import Product
from .category import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'qty_stock', 'category']
