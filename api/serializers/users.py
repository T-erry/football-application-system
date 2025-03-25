from rest_framework import serializers
from users .models import User


class UserSerializer(serializers.ModelSerializer):
    #custom id to hash our id's
    id = serializers.UUIDField(source='public_id', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', "last_name", 'email', "is_staff" , "is_active", 'is_superuser', 'date_joined', "updated"]


