# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from . import models, serializers

#Permisos
"""
class RecetasPermissions(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return user.has_permission('apis.add_receta')
        elif view.action == 'list':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if view.action == 'retrieve':
            return user.has_permission('apis.view_receta') or user == obj.created_by
        elif view.action == 'destroy':
            return user.has_permission('apis.remove_receta')
        elif view.action == 'partial_update':
            return user.has_permission('apis.change_receta', obj) or user.has_permission('apis.change_receta')
        elif view.action == 'send_reminder':
            return True
        return False
"""
      
class CategoriaModelViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = [permissions.AllowAny, ]
    
class RecetaModelViewSet(viewsets.ModelViewSet):
    queryset = models.Receta.objects.all()
    serializer_class = serializers.RecetaSerializer
    permission_classes = [permissions.AllowAny]

