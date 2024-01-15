from django import forms #ayudra a crear formularios

from .models import Prueba #importamos el modelo prueba
#escribir codigo python que se conectecon los campos del form

class PruebaForm(forms.ModelForm): #usamos la clase Form
    """Form definition fo Prueba."""

    class Meta: #usamos el meta 
        """Meta definition fo Pruebaform."""

        model  = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        
        #para mas personalizacion como agregar placeholder etc utilizaremos witgets
    
        widgets={
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui'
                
                }
            )
        
        }
    
    #para validare un campo que el numero no se mejor a 10
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad <10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
            
        return cantidad #devuelve la misma cantidad
        
          
        
            
        
