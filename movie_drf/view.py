from rest_framework import permissions,views
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import serializers




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)
    
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)
        return token
  

class TokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer

