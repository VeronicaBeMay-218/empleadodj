from django.db import models
from applications.departamento.models import Departamento #importamos el modelo departamento
from ckeditor.fields import RichTextField #sirvepara la hoja de vida el campo para texto
#ckeditor app deterceros 

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta: #class meta sirve para cambiar como se va ver los nombres en el admin
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades empleados'
     
    def __str__(self): #siempre ponerlo
        return str(self.id) + '-' +self.habilidad
      
# Create your models here.

class Empleado(models.Model):
    """ Modelo para la tabla empleado """
    
    #job chiices para un select
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )
    #Contador
    #Administrador
    #eCONOMISTA
    #Otro
    #atributos de empleado
    first_name= models.CharField(('Nombres'), max_length=60)
    last_name= models.CharField(('Apellidos'), max_length=60)
    full_name= models.CharField( #nombre completo es un extra
        'Nombres completos', 
        max_length=120,
        blank=True #no es obligatorio
    )
    #resultado de concatenar first_name y last_name
    
    #mas atributos
    job= models.CharField(("Trabajo"), max_length=1, choices=JOB_CHOICES) #da la lista asignada en el job_choices
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)#relacion 1 a *
    avatar=models.ImageField(upload_to='empleado', blank=True, null=True) #para imagenes
    habilidades = models.ManyToManyField(Habilidades) #realcion * a * 
    hoja_vida= RichTextField() #campo de texto 
    
    #si8empre que se agregue algo hacer el migrate
    
    
    
    class Meta: #meta para cambiar los nombres, si ira ordenado como
        verbose_name='Mi Empleado'
        verbose_name_plural='Empleados de la empresa'
        ordering=['-first_name', 'last_name']
        unique_together=('first_name', 'departamento') #que los atributos sean unicos
    
    def __str__(self): #siempre hacerlo para string
            return str(self.id) + '-' +self.first_name + '-' + self.last_name
        