from django.urls import path

from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('crear-empleado', views.CrearEmpleadoView.as_view(), name='crear_empleado'),
]