from django.shortcuts import render
#
from django.views.generic import FormView, View, UpdateView
#
from .forms import UsuarioForm, LoginForm, CambiarContrasenaForm
#
from .models import Usuario
#
from django.urls import reverse_lazy, reverse
#
from django.http import HttpResponseRedirect
#
from django.contrib.auth import login, logout, authenticate
# Create your views here.


class CrearUsuarioView(FormView):
    form_class = UsuarioForm
    template_name = 'user/crear-usuario.html'
    success_url = reverse_lazy('users_app:login')


    def form_valid(self, form):
        Usuario.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
        )

        return super(CrearUsuarioView, self).form_valid(form)


class LoginUsuarioView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('hombe_app:index')


    def form_valid(self, form):
        usuario = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )

        login(self.request, usuario)

        return super(LoginUsuarioView, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )



class ActualziarPasswordView(FormView):
    form_class = CambiarContrasenaForm
    template_name = 'user/cambiar-password.html'
    success_url = reverse_lazy('users_app:login')

    def get_form_kwargs(self):
        kwargs =  super(ActualziarPasswordView, self).get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs
    
    
    def form_valid(self, form):
        usuario = self.request.user
        password = form.cleaned_data['new_password']

        usuario.set_password(password)
        usuario.save()

        logout(self.request)

        return super(ActualziarPasswordView, self).form_valid(form)