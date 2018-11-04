# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User

from . import models, serializers

# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny, ]
    
    
class FavsUserModelViewSet(viewsets.ModelViewSet):
    queryset = models.FavsUser.objects.all()
    serializer_class = serializers.FavsUserSerializer
    permission_classes = [permissions.AllowAny, ]
    