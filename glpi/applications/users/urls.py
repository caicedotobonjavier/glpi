from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path('crear-usuario', views.CrearUsuarioView.as_view(), name='crear'),
    path('login', views.LoginUsuarioView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('actualizar-pass', views.ActualziarPasswordView.as_view(), name='actualizar'),
]
