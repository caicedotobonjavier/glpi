from django.shortcuts import render
#
from django.views.generic import FormView
#
from .forms import EmpleadoForm
#
from .models import Empleado


class CrearEmpleadoView(FormView):
    form_class = EmpleadoForm
    template_name = 'empleado/crear-empleado.html'
    success_url = '.'


    def form_valid(self, form):
        Empleado.objects.create(
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            tipo_documento = form.cleaned_data['tipo_documento'],
            numero_documento = form.cleaned_data['numero_documento'],
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],    
            direccion = form.cleaned_data['direccion'],
            email = form.cleaned_data['email'],
            area = form.cleaned_data['area'],
            profesion = form.cleaned_data['profesion'],
            cargo = form.cleaned_data['cargo'],
            foto = form.cleaned_data['foto'],
        )
        

        return super(CrearEmpleadoView, self).form_valid(form)