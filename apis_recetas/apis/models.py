from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,blank=True)

class Receta(models.Model):
    nombre      = models.CharField(max_length=50,blank=True)
    ingrediente = models.TextField()
    categoria_id= models.ForeignKey(Categoria,on_delete=models.CASCADE)
    preparacion = models.TextField()
    
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recetas_fav = models.ManyToManyField(Receta, related_name = u'favoritas', through='Favorito')
    recetas_creadas = models.ManyToManyField(Receta,related_name = u'creadas', through='RecetasCreadas')

class Favorito(models.Model):
    usuario_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    receta_id  = models.ForeignKey(Receta,on_delete=models.CASCADE)

class RecetasCreadas(models.Model):
    usuario_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    receta_id  = models.ForeignKey(Receta,on_delete=models.CASCADE)
