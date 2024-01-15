from django import forms

from .models import Empleado

#vanmos a depender d un modelo

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        #campos que necesito para registar un empleado como esta en el template
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades'
        )
        
        widgets={
            'habilidades':forms.CheckboxSelectMultiple()
        
        
        }


