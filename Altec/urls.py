from django.urls import path
from Altec import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    
    path('crearPresupuesto',views.crearPresupuesto,name='crearPresupuesto'),
    path('presupuesto_precio', views.presupuesto_precio),
   
   
]

