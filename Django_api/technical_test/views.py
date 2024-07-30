from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Player, PlayerSkill
from .serializers import PlayerSerializer
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['POST', 'GET'])
def create_get_player(request):
    if request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HasValidToken(BasePermission):
    def has_permission(self, request, view):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            return token == 'SkFabTZibXE1aE14ckpQUUxHc2dnQ2RzdlFRTTM2NFE2cGI4d3RQNjZmdEFITmdBQkE='
        return False


@api_view(['PUT', 'DELETE','GET'])
def get_modify_delete_player(request, player_id):
    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response({"message": f"Player with id {player_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlayerSerializer(player)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            updated_player = serializer.save()
            return Response(PlayerSerializer(updated_player).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        auth_header = request.headers.get('Authorization')
        if auth_header != 'Bearer SkFabTZibXE1aE14ckpQUUxHc2dnQ2RzdlFRTTM2NFE2cGI4d3RQNjZmdEFITmdBQkE=':
            return Response({'detail': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)