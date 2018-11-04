from rest_framework import serializers
from . import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        exclude = []
        
class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Receta
        exclude = []
