from django.contrib import admin
#
from .models import Usuario
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'nombres',
        'apellidos',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
    )


admin.site.register(Usuario, UsuarioAdmin)