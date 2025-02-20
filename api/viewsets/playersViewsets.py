from rest_framework import viewsets
from api.serializers.players import PlayerSerializer
from players.models import Player
from rest_framework.exceptions import ValidationError



class PlayerListView(viewsets.ModelViewSet):

   http_method_names = ['get']

   serializer_class = PlayerSerializer

   queryset = Player.objects.all()


class PlayerSearchViewset(viewsets.ModelViewSet):
    http_method_names = ['get']

    serializer_class = PlayerSerializer

    queryset = Player.objects.all()

    def get_queryset(self):
        queryset = Player.objects.all()  # Start with all Player objects
        
        name = self.request.query_params.get("name")  # Get the "name" query parameter
        club = self.request.query_params.get("club")  # Get the "club" query parameter
        min_age = self.request.query_params.get("min_age")
        max_age = self.request.query_params.get("max_age")

        if name and len(name) < 2:
            raise ValidationError({"name": "Name must be atleast 2 characters"})

        if name:
            queryset = queryset.filter(name__contains=name)  # Filter by name (case-insensitive)
        
        if club:
            queryset = queryset.filter(club=club)  # Filter by club name (case-insensitive)
        
        if min_age and max_age:
            queryset = queryset.filter(age__range = (min_age, max_age))  # Filter by minimum age
        
       
        
        return queryset