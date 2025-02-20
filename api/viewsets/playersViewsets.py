from rest_framework import viewsets
from api.serializers.players import PlayerSerializer
from players.models import Player



class PlayerListView(viewsets.ModelViewSet):

   http_method_names = ['get']

   serializer_class = PlayerSerializer

   queryset = Player.objects.all()

