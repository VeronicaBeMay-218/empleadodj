from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView #importamos las vistasgenericasquese va a utilizar
from .models import Prueba#importamos el modelo prueba

from .forms import PruebaForm #importamos el forms de archivo forms la clase PruebaForm

# Create your views here.

class IndexView(TemplateView): #una clase simple para vista Seusa TemplateView
    template_name = 'home/home.html' #nomnbre del template html
    

class PruebaListView(ListView): #clase para listas se usa listView
    template_name = 'home/lista.html'
    queryset = ['A', 'B','C'] #que vamos a listar
    context_object_name= 'lista_prueba' #variable lista:prueba
    

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html" #direccion del template
    context_object_name= 'lita_prueba' #variable

    

class PruebaCreateView(CreateView): #para agregar un registro createView
    model = Prueba #va trabajar con un modelo
    template_name = "home/add.html" #en donde esta la el html
    form_class= PruebaForm #manejara un form - el form se haceaparte
    success_url = '/' #envia a inicio

    
class PruebaView(TemplateView): #para pobrar los estilos
    template_name = "home/prueba.html"
   
#para probar el sistema d grillas
class ResumeFoundationView(TemplateView): #para pobrar los estilos
    template_name = "home/resume_foundation.html"

class Home1View(TemplateView): #para pobrar los estilos
    template_name = "home/home1.html"
    
class Home2View(TemplateView): #para pobrar los estilos
    template_name = "home/home2.html"