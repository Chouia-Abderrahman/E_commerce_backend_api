from telnetlib import AUTHENTICATION

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_login(request):
    print('user is authorized, token is valid')
