from django.shortcuts import render
from Altec.models import *
from Altec.forms import *

# Create your views here.
def inicio(request):
    return render(request,'Altec/index.html')

def crearPresupuesto(request):
    if request.method == 'POST':

            miFormulario = CrearPresupuestos(request.POST) #aquí mellega toda la información del html

            

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  presupuesto = Presupuestos (superficie=informacion['superficie'], tipo_trabajo=informacion['tipo_trabajo']) 

                  presupuesto.save()

                  

                  return render(request, "Altec/presupuesto_precio.html",{'presupuesto':presupuesto}) #Vuelvo al inicio o a donde quieran

    else: 

            miFormulario= CrearPresupuestos() #Formulario vacio para construir el html

            return render(request, "Altec/index.html", {"miFormulario":miFormulario})


def presupuesto_precio(request):

    if request.GET['tipo_trabajo'] == 'Cerramientos':
    
        
        precio = 30*Presupuestos.superficie()
        presupuestoFinal={'precio':precio}

    elif request.GET['tipo_trabajo'] == 'Piletas':
        
        precio = 45*Presupuestos.superficie()
        presupuestoFinal={'precio':precio}

    elif request.GET['tipo_trabajo'] == 'Quinchos':
        
            
        precio = 25*Presupuestos.superficie()
        presupuestoFinal={'precio':precio}

    elif request.GET['tipo_trabajo'] == 'Techos':
         

        precio = 80*Presupuestos.superficie()
        presupuestoFinal={'precio':precio}

    return render(request,'presupuestoFinal.html',presupuestoFinal)