from rest_framework import serializers
from users .models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    #custom id to hash our id's
    id = serializers.UUIDField(source='public_id', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', "last_name", 'email', "is_staff" , "is_active", 'is_superuser', 'date_joined', "updated"]


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'email', 'password']
        
    #Responsible for creating our user
    def create(self, validated_data):
        
       user = User.objects.create_user(**validated_data)

    #    user = User.create_user(
    #           email=validated_data['email'],
    #           first_name=validated_data['first_name'],
    #           last_name=validated_data['last_name'],
    #           password=validated_data['password']
    #    )

       return user