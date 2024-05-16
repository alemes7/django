from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('reserve', views.reserve, name='reserve'),
    path('nome', views.nome, name='nome'),
    path('solteiro', views.solteiro, name='solteiro'),
    path('casal', views.casal, name='casal'),
    path('comfort', views.comfort, name='comfort'),
    path('luxo', views.luxo, name='luxo')
]