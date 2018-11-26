from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    
        
class FavsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavsUser
        exclude = []