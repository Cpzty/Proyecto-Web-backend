from django.db import models
from django.contrib.auth.models import User


#Permisos
"""
class RecetaPermissions(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return user.has_permission('canoneras.add_canonera')
        elif view.action == 'list':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if view.action == 'retrieve':
            return user.has_permission('canoneras.view_canonera') or user == obj.created_by
        elif view.action == 'destroy':
            return user.has_permission('canoneras.remove_canonera')
        elif view.action == 'partial_update':
            return user.has_permission('canoneras.change_canonera', obj) or user.has_permission('canoneras.change_canonera')
        elif view.action == 'send_reminder':
            return True
        return False

"""


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,blank=True)


class Receta(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    ingrediente = models.TextField()
    preparacion = models.TextField()
    categoria_id= models.ForeignKey(Categoria, models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE )

