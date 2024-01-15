from typing import Any
from django.db.models.query import QuerySet #importamos para usar queryset
from django.shortcuts import render#Esta función recibe como argumento, de forma obligatoria, 3 valores. La petición per se, el template a renderizar y un contexto. El contexto no será más que un diccionario cuyas llaves podrán ser utilizadas dentro del template.
from django.urls import reverse_lazy #para las url sean cortas y esteticas
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView #imporatacion de vistar genericas que se van a usar

#models
from .models import Empleado#vamos a trabajar directamente con el modelo empleado

#forms
from .forms import EmpleadoForm
#clase para la primera vista completa empleados


class InicioView(TemplateView):
    """vista que carga la pagina de inicio"""
    template_name = "inicio.html"#no esta dentro de ninguna carpeta


#para que muestre en la vista a los empleados de 4 en 4

   #si nosotros estamos sobreescribiendo el metodo queriset ya no serannecesario pasarle l model de nuestro list view
    #model= Empleado #para todos lo0s empleados
    
    #buscador para esta vista
    #en el html en el inputhayque iddicar el id="kword" yel name="kword"
    #quiero filtrar el full_name
    #jorge= j lo que hace icontains es uscar j dentrod de la cadena jorge
    #lo que tenga palabra_clave lo esta buscando dentro de full_name
    #siempre va buscar cadena que sean similitudes y que esten dentro de esta otra cadena
class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by= 4
    ordering= 'first_name'
    context_object_name= 'empleados'
      
    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword", '')
        lista=Empleado.objects.filter(
            full_name__icontains=palabra_clave   
        )
        return lista
        
        
#copiamos lo de arriba xq es similar pra administrar

class ListaEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by= 10
    ordering= 'first_name'
    context_object_name= 'empleados'#mismo
    model = Empleado #al no tener el qryset necesitamos indicar el modelo
    
    #ya no quiero que haga el filtro xq e este caso vamos a listar todo y no vamos  filtrar por algun parametro en particular
    # get_queryset(self):
        #palabra_clave=self.request.GET.get("kword", '')
        #lista=Empleado.objects.filter(
            #full_name__icontains=palabra_clave   
        #)
        #return lista
        
    
        
 
 #listamos losempreados segun su area
class ListByAreaEmpleado(ListView):
    """lista empleados de un area"""
    template_name='persona/list_by_area.html'
    context_object_name='empleados'
     #usar queryset
    
    #otra forna de hace filtro en la ligaagregamos /contabilidad con este filtro
    def get_queryset(self):
        area=self.kwargs['shorname']
        lista=Empleado.objects.filter(
            departamento__shor_name=area
    )
        return lista
        
        
#aun no funciona
class ListByTrabajoEmpleado(ListView):
    """lista empleados de un trabajo"""
    template_name='persona/list_by_trabajo.html'
     #usar queryset
     
    def get_queryset(self):
        #Trabajo=self.kwargs['job']
        lista2=Empleado.objects.filter(
            job='OTRO'
    )
        return lista2


#en esta vista usamos ub buscador
class ListEmpleadosByKword(ListView):
    """Lista empleado por palabra clave """
    template_name='persona/by_kword.html'
    context_object_name= 'empleados'
    
       
#para el buscador en una vista
    def get_queryset(self):
        
        print('*******************')
        palabra_clave=self.request.GET.get("kword", '')
        lista=Empleado.objects.filter(
            first_name=palabra_clave
        )
    
        return lista
       
#para las habilidades
class ListHabilidadesEmpleado(ListView):
    template_name='persona/habilidades.html'
    context_object_name='habilidades'
    
    def get_queryset(self):
        #logica pararetornar - muchos a muchos
        empleado= Empleado.objects.get(id=9)#recuperado un registrosolo se requiere un registro se usa get
    
        return empleado.habilidades.all()




# Create your views here.
#1 listar todos los empleados de la empresa
#2 listar todos los empleados que pertenecen a un area de la empresa
#3.listar empleador por trabajo
#4. listar los empleados por palabra clave
#5. listar habilidades de un empleado


#mostrar maas detalles de un empleado agregra cono una texto 
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs): 
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] =  'Empleado del mes'
        return context


#classe para la vista de que algo se guardo correctament6e
class SucessView(TemplateView):
    template_name = "persona/sucess.html"
    
#para crear el form de maner automatica
class EmpleadoCreateView(CreateView):
    template_name="persona/add.html"
    model=Empleado
    form_class=EmpleadoForm
     # para todo('__all__')
    success_url= reverse_lazy('persona_app:empleados_admin')#nos manda al url correcto #redirecccion
    
    #una nueva necesidad
    def form_valid(self, form):#para unir nombre con apellido y gusrdarlo en la base de datos
    #loogicadel proceso
        empleado=form.save(commit=False)
        empleado.full_name=empleado.first_name + ' ' + empleado.last_name
        
        #para que se gusrde en la base de datos
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
  

class EmpleadoUpdateView(UpdateView): #updateview para  actualizary crear el form
    template_name = "persona/update.html"
    model = Empleado
    fields=[ #que atribustossaldran en el form
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    
    ] 
    
    success_url= reverse_lazy('persona_app:empleados_admin')#nos manda al url correcto
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***********METODO POST***********')
        print('=====================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    #una nueva necesidad
    def form_valid(self, form):#para unir nombre con apellido y gusrdarlo en la base de datos
    #loogicadel proceso-SOBREESCRIBIR DENTRO DE ESTE MEDIO
        print('***********METODO FORM VALID***********')
        print('****************************')
        return super(EmpleadoUpdateView, self).form_valid(form)
    
    

class EmpleadoDeleteView(DeleteView):#para elimminar, no elimina necesita un confirmacion
    model = Empleado
    template_name = "persona/delete.html"
    success_url= reverse_lazy('persona_app:empleados_admin')#nos manda al url correcto




    
