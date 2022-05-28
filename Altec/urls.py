from django.urls import path
from Altec import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('borrar_presupuesto', views.borrar_presupuestos, name="borrarPresupuesto"),
    path('crearPresupuesto',views.crearPresupuesto,name='crearPresupuestos'),
    path('buscadorPresupuestos',views.buscador_presupuestos,name='buscadorPresupuestos'),
    path('empleados', views.lista_empleados,name="empleados"),
    path('editar_empleado/<empleados_id>', views.editar_empleados,name="editar-empleado"),
    path('borrar_empleado/<empleados_id>', views.borrar_empleados,name="borrar-empleado"),
    
   
   
]

