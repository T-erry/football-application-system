from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from users .models import User
from api.serializers.users import UserSerializer, RegisterSerializer, LoginSerializer


class UserViewset(viewsets.ModelViewSet):

    http_method_names =['get', 'patch', "delete"]

    serializer_class = UserSerializer

    queryset = User.objects.all()


    def get_object(self):
        user = User.objects.get_object_by_public_id(self.kwargs['pk'] )
        return user
    
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


