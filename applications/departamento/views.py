from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import FormView #esta a un nivel mas bajo
from applications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm #imporatamos el formulario


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name='departamentos'


class NewDepartamentoView(FormView):
    template_name= 'departamento/new_departamento.html'
    form_class= NewDepartamentoForm #necesitamos un formulario que reciba los datos
    success_url= '/' # es un resgirtro entonces necesita de un url ponemos el url de prueba
    
    #sobreescribir la funcion
    def form_valid(self, form):
        print('=======ESTAMOS EN EL FORM VALID=======')
        #instancia para asignarlo
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['departamento']
        )
        depa.save()#para que se guarde
        
        nombre= form.cleaned_data['nombre']
        apellido= form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa #la instancia creada
        )
        return super(NewDepartamentoView, self).form_valid(form) #return el forn valid de sobreescibe
        
#PARA CHECARQ ESO FUNCIONA HAY QUE CREAR EL URL