from django.contrib import admin
from.models import Empleado, Habilidades #importamos tabla
# Register your models here.


admin.site.register(Habilidades) #para que habilidades salga en la vista

class EmpleadoAdmin(admin.ModelAdmin):#una lista en columnas
    list_display=(
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    
    #
    def full_name(self, obj):
    #toda la operacion
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name
    
    search_fields=('first_name',) #buscador busqueda de acuerdo al nombre
    list_filter=('departamento','job','habilidades')#crear un filtro
    
    filter_horizontal=('habilidades',) #filtro solo funciona para * a *, lleva coma porque es una tupla
    
admin.site.register(Empleado, EmpleadoAdmin)