from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Player, PlayerSkill
from .serializers import PlayerSerializer
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from django.db.models import Max, F

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


@api_view(['POST'])
def process_team(request):
    requirements = request.data
    selected_players = []
    used_player_ids = set()

    for req in requirements:
        position = req['position']
        main_skill = req['mainSkill']
        number_of_players = req['numberOfPlayers']

        # Check if there are enough players for this position
        available_players = Player.objects.filter(position=position).exclude(id__in=used_player_ids)
        if available_players.count() < number_of_players:
            return Response({
                "message": f"Insufficient number of players for position: {position}"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Find players with the main skill
        players_with_skill = available_players.filter(skills__skill=main_skill)

        if players_with_skill.exists():
            # If players with the main skill exist, select the best ones
            best_players = players_with_skill.annotate(
                skill_value=F('skills__skill_level')).order_by('-skill_value')[:number_of_players]
        else:
            # If no players with the main skill, select based on highest skill
            best_players = available_players.annotate(
                max_skill=Max('skills__skill_level')
            ).order_by('-max_skill')[:number_of_players]

        for player in best_players:
            selected_players.append(player)
            used_player_ids.add(player.id)

    # Serialize the selected players
    serializer = PlayerSerializer(selected_players, many=True, context={'main_skill': req['mainSkill']})
    return Response(serializer.data)