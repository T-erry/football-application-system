from django.shortcuts import render
from rest_framework import routers
from api.viewsets.playersViewsets import PlayerListView, PlayerSearchViewset
from api.viewsets.usersViewsets import UserViewset, RegisterViewset

# Create your views here.

routes = routers.SimpleRouter()

routes.register('players', PlayerListView, basename="players"),
routes.register('search', PlayerSearchViewset, basename='Search'),
routes.register('users', UserViewset, basename="users"),
routes.register('auth/register', RegisterViewset, basename="register")

urlpatterns = routes.urls

#Api URLConf
