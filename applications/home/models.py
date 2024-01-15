from django.db import models

# Create your models here.
class Prueba(models.Model):#class preubas es como una tabla
    titulo = models.CharField(max_length=100) #cusndo es texto es charfield
    subtitulo = models.CharField(max_length=50) 
    cantidad= models.IntegerField()
    
    def __str__(self): #solo los q son texto esto siempre va
        return self.titulo + '-' + self.subtitulo
    

    