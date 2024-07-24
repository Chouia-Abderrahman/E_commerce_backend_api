from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def create_product(request):
    print("function_runs")
    return Response({'message': 'create_product'})

@api_view(['POST'])
def read_product(request):
    print("function_runs")
    return Response({'message': 'read_product'})
