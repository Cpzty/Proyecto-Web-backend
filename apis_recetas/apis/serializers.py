from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        exclude = []
        
class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Receta
        exclude = []
      
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        exclude = []
        
class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favorito
        exclude = []
        
class RecetasCreadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RecetasCreadas
        exclude = []