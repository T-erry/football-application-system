from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from users .models import User
from api.serializers.users import UserSerializer, RegisterSerializer, LoginSerializer
from players.models import Player
from api.serializers.players import PlayerSerializer
from api.permissions import UserPermissions

class UserViewset(viewsets.ModelViewSet):
    permission_classes= [UserPermissions]

    http_method_names =['get', 'patch', "delete", 'post']

    serializer_class = UserSerializer

    queryset = User.objects.all()


    def get_object(self):
        user = User.objects.get_object_by_public_id(self.kwargs['pk'] )
        # Check permissions against this specific user object
        self.check_object_permissions(request=self.request, obj=user)
        return user
    

    @action(detail=True, methods=['post'])
    def toggle_favorite(self, request, pk=None):

        player_id = request.data.get('player_id')

        user = self.get_object()

        if player_id:
            try:
                player = Player.objects.get(id=player_id)
            except Player.DoesNotExist:
                return Response({"Error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
          #to check if users have favorited the players  
            if user.favorite_players.filter(id=player_id).exists():

                user.favorite_players.remove(player)

                user.save()
                
                player_data = PlayerSerializer(player).data

                return Response({"message": "Player removed from favorites", "player_data": player_data}, status=status.HTTP_200_OK)
            else:  
                user.favorite_players.add(player)

                user.save()
                player_data = PlayerSerializer(player).data

                return Response({"message":"Player added to favorites", "player_data": player_data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Please provide a valid player id"}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=True, methods=['get'])
    def list_favorites(self, request, pk=None):

        user = self.get_object()

        favorites = user.favorite_players.all()

        # many=True to let the serializer know that it is dealing with multiple instances
        serializer = PlayerSerializer(favorites, many=True)

        return Response(serializer.data)


class RegisterViewset(viewsets.ViewSet):

    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
              "user" : serializer.data,  
            },

            status=status.HTTP_201_CREATED

        )

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({"message":"This view is protected"}, status=status.HTTP_201_CREATED)

class PublicView(APIView):

    def get(self, request):

        return Response({"message":"This is a public view"}, status=status.HTTP_201_CREATED)

class LoginView(viewsets.ViewSet):
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs ):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)

        except TokenError as e:
            raise InvalidToken(e)
        

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


