from django.shortcuts import render, HttpResponse #render, renderiza a pagina html e HttpResponse, retorna uma resposta ao cliente
from .models import Hotel #importa o model hotel
from .models import quarto #importa o model quarto

# Create your views here.
def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context['dados_hotel'] = dados_hotel
    return render(request, 'homepage.html', context) #retorna a pagina homepage.html

def reserve(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'reserve.html', context) #retorna a pagina quartos.html