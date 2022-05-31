from django.db import models

# Create your models here.
class Empleados(models.Model):
    rol = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    sueldo=models.IntegerField()
    comision = models.FloatField()
    acargo= models.IntegerField()
    profile_pic=models.ImageField(upload_to='media/',blank=True,null=True)

    def __str__(self):
        return f'Este empleado es un ' +self.rol + ' ,se llama ' + self.nombre + ', tiene un sueldo de ' + str(self.sueldo) + ', tiene una comisión porcentual de '+str(self.comision)+' y tiene ' + str(self.acargo )+ ' personas a cargo.'
        
    
class TrabajosHechos(models.Model):
    direccion = models.CharField(max_length=50)
    cobrado = models.IntegerField()
    email= models.EmailField()
    telefono=models.IntegerField()

    def __str__(self):
        return 'Este trabajo se hizo en ' +self.direccion + ' ,se cobró ' + self.cobrado + '. El mail de contacto es ' + self.email + 'y el teléfono es '+self.telefono

class Presupuestos(models.Model):
    #Se pide la superficie, luego el tipo de trabajo y dentro de cada tipo de trabajo, el tipo de materiales que se van a utilizar con su precio por metro cuadrado. 
    #Por ultimo, el tercer elemento de la clase (precio) lo calculo como : superficie * (precio_m^_materiales)
    superficie=models.FloatField()

    class TiposTrabajo(models.TextChoices):
        cerramientos = 'Cerramientos'
        piletas='Piletas'
        quinchos='Quinchos'
        techos='Techos'
        
    
    tipo_trabajo = models.CharField(choices= TiposTrabajo.choices, max_length=40)

    precio=models.FloatField(null=True)

    def __str__(self):
        return 'El presupuesto para una superficie de ' + str(self.superficie) + ' m^2, para el tipo de trabajo ' + self.tipo_trabajo + ' es de ' + str(self.precio) + ' pesos.'



