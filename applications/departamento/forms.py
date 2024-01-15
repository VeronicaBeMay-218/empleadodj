from django import forms #ayudra a crear formularios

#escribir codigo python que se conectecon los campos del form

class NewDepartamentoForm(forms.Form): 
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)
    
    