from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,blank=True)

class Receta(models.Model):
    nombre      = models.CharField(max_length=50,blank=True)
    ingrediente = models.TextField()
    categoria_id= models.ForeignKey(Categoria,on_delete=models.CASCADE)
    preparacion = models.TextField()

class User(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    correo = models.CharField(max_length=50,blank=True)
    passw = models.CharField(max_length=50,blank=True)
    recetas = models.ManyToManyField(Receta,through='Favorito')



class Favorito(models.Model):
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE)
    receta_id  = models.ForeignKey(Receta,on_delete=models.CASCADE)
