from django import forms
#
from .models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'nombres',
            'apellidos',           
            'tipo_documento',
            'numero_documento',
            'fecha_nacimiento',            
            'direccion',
            'email',
            'area',
            'profesion',
            'cargo',
            'foto',
        )

        widgets = {
            'nombres' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre del empledo'
                }
            ),
            'apellidos' : forms.TextInput(
                attrs={
                    'placeholder' : 'Apellidos del empledo'
                }
            ),
            'numero_documento' : forms.TextInput(
                attrs={
                    'placeholder' : '# Documento del empledo'
                }
            ),
            'fecha_nacimiento' : forms.TextInput(
                attrs={
                    'type' : 'date'
                }
            ),
            'direccion' : forms.TextInput(
                attrs={
                    'placeholder' : 'Direccion del empleado'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'ejemplo@email.com'
                }
            ),
        }