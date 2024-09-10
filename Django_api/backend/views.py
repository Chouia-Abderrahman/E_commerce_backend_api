from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def create_product(request):
    print("function_runs")
    return Response({'message': 'create_product'})

@api_view(['POST'])
def read_product(request):
    print("function_runs")
    return Response({'message': 'read_product'})
