from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ...models import Product
from ...serializers import ProductSerializer


@api_view(['GET'])
def products_by_category(request, categoryId):
    products = Product.objects.filter(category_id=categoryId)

    if products.exists():
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "No products found for this category."}, status=status.HTTP_404_NOT_FOUND)
