from django.contrib import admin
#
from .models import Area
# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_area',
        'nombre_area_corto',
    )


admin.site.register(Area, AreaAdmin)