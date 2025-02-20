from django.shortcuts import render
from rest_framework import routers
from api.viewsets.playersViewsets import PlayerListView

# Create your views here.

routes = routers.SimpleRouter()

routes.register('players', PlayerListView, basename="players")

urlpatterns = routes.urls

#Api URLConf
