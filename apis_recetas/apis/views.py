# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from . import models, serializers

"""
class CategoriaModelViewSet(generics.ListCreateAPIView):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    
    @classmethod
    def get_extra_actions(cls):
        return []
      
    
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    
    """
    
class CategoriaModelViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = [permissions.AllowAny, ]
    
class RecetaModelViewSet(viewsets.ModelViewSet):
    queryset = models.Receta.objects.all()
    serializer_class = serializers.RecetaSerializer
    permission_classes = [permissions.AllowAny, ]
    
class CustomUserModelViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [permissions.AllowAny, ]
    
class FavoritoModelViewSet(viewsets.ModelViewSet):
    queryset = models.Favorito.objects.all()
    serializer_class = serializers.FavoritoSerializer
    permission_classes = [permissions.AllowAny, ]
      
class RecetasCreadasModelViewSet(viewsets.ModelViewSet):
    queryset = models.RecetasCreadas.objects.all()
    serializer_class = serializers.RecetasCreadasSerializer
    permission_classes = [permissions.AllowAny, ]
    
