from django.db import models
from django.contrib.auth.models import User
from apis import models as apis_models
#from favs import models
# Create your models here.

class FavsUser(models.Model):
    user = models.ManyToManyField(User,related_name = u'usuario')
    receta_fav = models.ManyToManyField(apis_models.Receta, related_name = u'favoritas')
    #recetas_creadas = models.ManyToManyField(apis_models.Receta,related_name = u'creadas', through='apis_models.RecetasCreadas')

"""
class RecetasUsuarios(models.Model):
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE)
    receta_id  = models.ForeignKey(apis_models.Receta,on_delete=models.CASCADE)
"""    
