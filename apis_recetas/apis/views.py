# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from . import models, serializers
    
class CategoriaModelViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = [permissions.AllowAny, ]
    
class RecetaModelViewSet(viewsets.ModelViewSet):
    queryset = models.Receta.objects.all()
    serializer_class = serializers.RecetaSerializer
    permission_classes = [permissions.AllowAny, ]

