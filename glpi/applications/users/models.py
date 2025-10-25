from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UsuarioManager
# Create your models here.

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre Usuario', max_length=50, unique=True)
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    email = models.EmailField('Correo Electronico', max_length=254)

    is_active = models.BooleanField('Activo', default=False)
    is_staff = models.BooleanField('Staff', default=False)
    is_superuser = models.BooleanField('Super Usuario', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UsuarioManager()


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    

    def __str__(self):
        return self.username