from django.shortcuts import render, HttpResponse #render, renderiza a pagina html e HttpResponse, retorna uma resposta ao cliente
from .models import Hotel #importa o model hotel
from .models import quarto #importa o model quarto
from .forms import FormNome #importa o form nome
from .models import Usuario #importa o model usuario

# Create your views here.
def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context['dados_hotel'] = dados_hotel
    return render(request, 'homepage.html', context) #retorna a pagina homepage.html

def reserve(request):
    context = {}
    tipos_quartos = ['SOLTEIRO', 'CASAL', 'CONFORTO', 'LUXO']
    dados_quartos = []

    for tipo in tipos_quartos:
        quarto_tipo = quarto.objects.filter(tipo=tipo).first()
        if quarto_tipo:
            dados_quartos.append(quarto_tipo)

    context['dados_quarto'] = dados_quartos
    return render(request, 'reserve.html', context)

def solteiro(request):
    context = {}
    dados_quarto = quarto.objects.filter(tipo='SOLTEIRO')
    context['dados_quarto'] = dados_quarto
    return render(request, 'solteiro.html', context) #retorna a pagina solteiroo.html

def casal(request):
    context = {}
    dados_quarto = quarto.objects.filter(tipo='CASAL')
    context['dados_quarto'] = dados_quarto
    return render(request, 'casal.html', context) #retorna a pagina casal.html

def comfort(request):
    context = {}
    dados_quarto = quarto.objects.filter(tipo='CONFORTO')
    context['dados_quarto'] = dados_quarto
    return render(request, 'comfort.html', context) #retorna a pagina comfort.html

def nome(request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['senha']

            user = Usuario(nome=var_nome, email=var_email, senha=var_senha)
            user.save()

            print(var_nome)
            print(var_email)
            print(var_senha)

            return HttpResponse("<h1>thanks</h1>")
    else:
        form = FormNome()

        return render(request, "nome.html", {"form": form})