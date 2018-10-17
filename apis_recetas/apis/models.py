from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre  = models.CharField(max_length=50,blank=True)

class Receta(models.Model):
    nombre      = models.CharField(max_length=50,blank=True)
    ingrediente = models.TextField()
    categoria_id= models.ForeignKey('Categoria',on_delete=models.CASCADE)
    preparacion = models.TextField() 
