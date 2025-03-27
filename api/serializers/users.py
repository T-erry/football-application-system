from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import update_last_login

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
    
class LoginSerializer(TokenObtainPairSerializer): 
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(user=self.user)

        user = UserSerializer(self.user).data

        data['refresh'] = str(refresh)

        data['access'] =  str(refresh.access_token)

        data['user'] = user

        # This function helps track user activity by updating the `last_login` field whenever a user logs in.
        update_last_login(None, self.user)


        return data
