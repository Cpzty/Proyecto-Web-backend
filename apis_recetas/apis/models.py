from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,blank=True)


class Receta(models.Model):
    nombre = models.CharField(max_length=50,blank=True, null=False)
    ingrediente = models.TextField()
    preparacion = models.TextField()
    categoria_id= models.ForeignKey(Categoria, models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE )

