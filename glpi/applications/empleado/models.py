from django.db import models
#
from applications.area.models import Area
#
from applications.users.models import Usuario
#
from django.db.models.signals import post_save, pre_save
#
from datetime import date
# Create your models here.

CC = '1'
PP = '2'
CE = '3'
PEP = '4'

CHOICES_TIPO_DOC = (
    (CC, 'Cedula'),
    (PP, 'Pasaporte'),
    (CE, 'Cedula Extranjeria'),
    (PEP, 'Permiso Especial de Permanencia'),
)

ABOGADO = '1'
INGENIERO_SISTEMAS = '2'
CONTADOR = '3'
TECNOLOGO_SISTEMAS = '4'
PROFESIONAL_SST = '5'
PUBLISISTA = '6'
TECNOLOGO_GESTION_ADMINISTRATIVA = '7'

CHOICES_PROFESION = (
    (ABOGADO, 'Abogado'),
    (INGENIERO_SISTEMAS, 'Ingeniero Sistemas'),
    (CONTADOR, 'Contador'),
    (TECNOLOGO_SISTEMAS, 'Tecnologo Sistemas'),
    (PROFESIONAL_SST, 'Profesion Seguridad Salud Trabajo'),
    (PUBLISISTA, 'Publisista'),
    (TECNOLOGO_GESTION_ADMINISTRATIVA, 'Tecnolgo Gestion Administrativa'),
)

AUXILIAR = '1'
TECNICO = '2'
TECNOLOGO = '3'
PROFESIONAL = '4'
ESPECIALISTA = '5'
DIRECTOR = '6'
GERENTE = '7'

CHOICES_CARGO = (
    (AUXILIAR, 'Auxiliar'),
    (TECNICO, 'Tecnico'),
    (TECNOLOGO, 'Tecnologo'),
    (PROFESIONAL, 'Profesional'),
    (ESPECIALISTA, 'Especialista'),
    (DIRECTOR, 'Director'),
    (GERENTE, 'Gerente'),
)

class Empleado(models.Model):
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    nombre_completo = models.CharField('Nombre Completo', max_length=50, null=True, blank=True)
    tipo_documento = models.CharField('Tipo Documento', max_length=1, choices=CHOICES_TIPO_DOC)
    numero_documento = models.CharField('Numero Documento', max_length=50)
    fecha_nacimiento = models.DateField('Fecha Nacimiento', auto_now=False, auto_now_add=False)
    edad = models.PositiveIntegerField('Edad', null=True, blank=True)
    direccion = models.CharField('Direccion', max_length=50, null=True, blank=True)
    email = models.EmailField('Email', max_length=254)
    area = models.ForeignKey(Area, related_name='area_empleado', on_delete=models.CASCADE)
    profesion = models.CharField('Profesion', max_length=1, choices=CHOICES_PROFESION)
    cargo = models.CharField('Cargo', max_length=1, choices=CHOICES_CARGO)
    foto = models.ImageField('Foto', upload_to='Fotos', height_field=None, width_field=None, max_length=None, null=True, blank=True)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(fields=['nombres', 'apellidos', 'numero_documento'], name='unique_empleado')
        ]        
    

    def __str__(self):
        return self.nombres
    

#signas
def complemento(sender, instance, **kwargs):
    nuevo = instance
    nuevo.nombre_completo = instance.nombres + ' ' + instance.apellidos
    nuevo.edad = date.today().year - nuevo.fecha_nacimiento.year

pre_save.connect(complemento, sender=Empleado)  