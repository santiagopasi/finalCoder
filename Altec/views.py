from django.shortcuts import render
from Altec.models import *
from Altec.forms import *
import random


# Create your views here.
def inicio(request):
    return render(request,'base.html')

def crearPresupuesto(request):
    if request.method == 'POST':

            mi_formulario =  CrearPresupuestos(request.POST)#aquí mellega toda la información del html
            
            if mi_formulario.is_valid():
                #esto me genera un diccionario con todos los campos del formulario
                diccionario = mi_formulario.cleaned_data
                
                
                if diccionario['tipo_trabajo'] == 'Cerramientos':
                    precio = 30*diccionario['superficie']
                elif diccionario['tipo_trabajo'] == 'Piletas':
                    precio = 45*diccionario['superficie']
                elif diccionario['tipo_trabajo'] == 'Quinchos':
                    precio = 25*diccionario['superficie']
                elif diccionario['tipo_trabajo'] == 'Techos':
                    precio = 80*diccionario['superficie']
                
            nuevo_valor=Presupuestos(superficie=diccionario['superficie'],tipo_trabajo=diccionario['tipo_trabajo'],precio=precio)  
            nuevo_valor.save()  
            mensaje=("Presupuesto creado con éxito. Su precio es de $" + str(precio))
            return render(request,'presupuesto.html',{'mensaje':mensaje})

    else: 

             #Formulario vacio para construir el html

            return render(request, "presupuesto.html")


def buscador_presupuestos(request):
    elementos=Presupuestos.objects.all()

    if request.POST.get('superficie',False):
        superficie = request.POST.get('superficie',False)

        superficie_busqueda = Presupuestos.objects.filter(superficie__icontains=superficie)

        return render(request, 'buscador_presupuestos.html', {'superficie_busqueda':superficie_busqueda})

    elif request.POST.get('tipo_trabajo',False):
        tipo_trabajo = request.POST.get('tipo_trabajo',False)

        tipo_trabajo_busqueda = Presupuestos.objects.filter(tipo_trabajo__icontains=tipo_trabajo)

        return render(request, 'buscador_presupuestos.html', {'tipo_trabajo_busqueda':tipo_trabajo_busqueda})
    else:   
   
        return render(request,'buscador_presupuestos.html',{'elementos':elementos})
    

def borrar_presupuestos(request):
    elementos=Presupuestos.objects.all()

    if request.POST.get('superficie',False):
            presupuesto = Presupuestos(request.POST)

            if presupuesto.is_valid():
                presupuesto.delete()
                return render(request, 'borrar_exito.html')

    else:
        return render(request,'buscador_presupuestos.html')

def lista_empleados(request):
    
    
    roles=['Administrador','Vendedor','Cajero','Gerente']
    santiago=Empleados(nombre='Santiago',rol="CEO",sueldo=500000,comision=0,acargo=13)
    julian=Empleados(nombre='Julian',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    daniel=Empleados(nombre='Daniel',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    lucas=Empleados(nombre='Lucas',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    rosa=Empleados(nombre='Rosa',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    eugenia=Empleados(nombre='Eugenia',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    celeste=Empleados(nombre='Celeste',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    enrique=Empleados(nombre='Enrique',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    alfonso=Empleados(nombre='Alfonso',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    roco=Empleados(nombre='Roco',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    jose=Empleados(nombre='Jose',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    javier=Empleados(nombre='Javier',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    juan=Empleados(nombre='Juan',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))
    josefina=Empleados(nombre='Josefina',rol=roles[random.randint(0,3)],sueldo=random.randint(80000,300000),comision=random.random(),acargo=random.randint(0,4))

    santiago.save()
    julian.save()
    daniel.save()
    lucas.save()
    rosa.save()
    eugenia.save()
    celeste.save()
    enrique.save()
    alfonso.save()
    roco.save()
    jose.save()
    javier.save()
    juan.save()
    josefina.save()

    empleados=Empleados.objects.all()
        
    return render(request,'empleados.html',{'empleados':empleados})