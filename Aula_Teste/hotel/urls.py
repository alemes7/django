from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('reserve', views.reserve, name='reserve'),
    path('nome', views.nome, name='nome'),
    path('solterio', views.solteiro, name='solteiro'),
]