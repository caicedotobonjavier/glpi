from django.db import models

# Create your models here.
class Area(models.Model):
    nombre_area = models.CharField('Nombre Area', max_length=50)
    nombre_area_corto = models.CharField('Nombre Area Corto', max_length=50)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        db_table = 'area'
        constraints = [
            models.UniqueConstraint(fields=['nombre_area', 'nombre_area_corto'],name='constrains_area')
        ]      
    

    def __str__(self):
        return self.nombre_area