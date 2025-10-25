from django.urls import path

from . import views

app_name = 'hombe_app'


urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
]
