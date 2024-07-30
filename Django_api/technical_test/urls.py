from django.urls import path
from .views import (create_player,
                    # update_player,
                    # delete_player,
                    modify_player,)

urlpatterns = [
    path('player/', create_player, name='create_player'),
    path('player/<int:player_id>/', modify_player, name='modify_player'),
    # path('player/<int:player_id>/', delete_player, name='delete_player'),
]