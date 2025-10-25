from django.contrib import admin
#
from .models import Empleado
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombres',
        'apellidos',
        'nombre_completo',
        'tipo_documento',
        'numero_documento',
        'fecha_nacimiento',
        'edad',
        'direccion',
        'email',
        'area',
        'profesion',
        'cargo',
        'foto',
    )


admin.site.register(Empleado, EmpleadoAdmin)