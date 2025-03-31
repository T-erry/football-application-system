from django.shortcuts import render
from rest_framework import routers
from api.viewsets.playersViewsets import PlayerListView, PlayerSearchViewset
from api.viewsets.usersViewsets import UserViewset, RegisterViewset, LoginView

# Create your views here.

routes = routers.SimpleRouter()

routes.register('players', PlayerListView, basename="players"),
routes.register('search', PlayerSearchViewset, basename='Search'),
#users/<pk>/toggle_favorite,
#users/<pk>/list_favorites,
routes.register('users', UserViewset, basename="users"),
routes.register('auth/register', RegisterViewset, basename="register")
routes.register('auth/login', LoginView, basename="login")

urlpatterns = routes.urls

#Api URLConf
