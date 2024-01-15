from django.urls import path
from . import views



#darle un eqtiquueta para acceder con una liga corta 
app_name="persona_app"

urlpatterns = [
    path(
        '', #como es la de inicio no sepone nada
        views.InicioView.as_view(), 
        name='inicio'  
    ),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
    ), 
    #direc asignda, nombre de la classe
    path(
        'listar-by-area/<shorname>',
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'
    ),
    path(
        'lista-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('listar-by-trabajo/', views.ListByTrabajoEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
        ),
        #se agrega pk porque se usara solo un registro en especifico
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
        ),
    path(
        'success/', #redireccionar
        views.SucessView.as_view(), 
        name='correcto'  
    ), #le manda al success, classe succesView y con nmbre correcto
    #asignarlo en la vista de esta forma: 'persona_app:correcto'
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'  
    ),
    path(
        'delete-empleado/<pk>/', #pk porq se va a eliminar 1
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'  
    ),
   
] 