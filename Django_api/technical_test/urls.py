from django.urls import path
from .views import (create_get_player,
                    get_modify_delete_player,)

urlpatterns = [
    path('player/', create_get_player, name='create_player'),
    path('player/<int:player_id>/', get_modify_delete_player, name='modify_player'),
    # path('player/<int:player_id>/', delete_player, name='delete_player'),
]