from django import forms
#
from .models import Usuario
#
from django.contrib.auth import authenticate

class UsuarioForm(forms.ModelForm):

    password = forms.CharField(
        label= 'Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Ingrese contraseña'
            }
        )
    )

    password_2 = forms.CharField(
        label= 'Confirmar Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirme contraseña'
            }
        )
    )

    class Meta:
        model = Usuario
        fields = (
            'username',
            'nombres',
            'apellidos',
            'email',
        )

        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre de usuario'
                }
            ),

            'nombres' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombres'
                }
            ),

            'apellidos' : forms.TextInput(
                attrs={
                    'placeholder' : 'Apellidos'
                }
            ),

            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'email@ejemplo.com'
                }
            )
        }

    
    def clean_password_2(self):
        password = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_2']
        if password != password_2:
            raise forms.ValidationError('No coinciden las contraseñas')



class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre Usuario',
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder' : 'Nombre de usuario'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña de usuario'
            }
        )
    )


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        usuario = authenticate(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password']
        )
        if not usuario:
            raise forms.ValidationError('Usuario o contraseña erronea')
        return cleaned_data



class CambiarContrasenaForm(forms.Form):
    password = forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña Actual'
            }
        )
    )

    new_password = forms.CharField(
        label='Nueva Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Nueva Contraseña'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        print(self.usuario)
        super(CambiarContrasenaForm, self).__init__(*args, **kwargs)
    

    def clean(self):
        cleaned_data = super(CambiarContrasenaForm, self).clean()
        usuario = authenticate(
            username = self.usuario,
            password = self.cleaned_data['password']
        )
        if not usuario:
            raise forms.ValidationError('Contraseña actual erronea')
        return cleaned_data