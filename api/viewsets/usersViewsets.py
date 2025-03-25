from rest_framework import viewsets
from users .models import User
from api.serializers.users import UserSerializer


class UserViewset(viewsets.ModelViewSet):

    http_method_names =['get', 'patch']

    serializer_class = UserSerializer

    queryset = User.objects.all()


    def get_object(self):
        user = User.objects.get_object_by_public_id(self.kwargs['pk'] )
        return user