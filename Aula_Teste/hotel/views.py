from django.shortcuts import render, HttpResponse #render, renderiza a pagina html e HttpResponse, retorna uma resposta ao cliente
from .models import Hotel #importa o model hotel
from .models import quarto #importa o model quarto
from .forms import FormNome #importa o form nome
from .forms import FormReserva #importa o form reserva
from .forms import FormLogin #importa o form login
from .models import Reserva_quarto #importa o model reserva_quarto
from django.contrib.auth.models import User #importa o model usuario do django
from django.contrib.auth import authenticate, login  #importa o authenticate e login do django

# Create your views here.

# Função que retorna a pagina homepage.html
def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context['dados_hotel'] = dados_hotel
    return render(request, 'homepage.html', context) #retorna a pagina homepage.html

#----------------------------------------------------------------------------------------------------------------------------

# Função que retorna a pagina reserve.html, onde aparece os principais quartos disponiveis
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

#----------------------------------------------------------------------------------------------------------------------------

# Função que retorna a pagina solteiro.html, onde aparece os quartos do tipo solteiro

def solteiro(request):
    context = {}
    dados_quarto = quarto.objects.filter(tipo='SOLTEIRO')
    context['dados_quarto'] = dados_quarto
    return render(request, 'solteiro.html', context) #retorna a pagina solteiroo.html

# ----------------------------------------------------------------------------------------------------------------------------

# Função que retorna a pagina casal.html, onde aparece os quartos do tipo casal

def casal(request):
    context = {}
    dados_quarto = quarto.objects.filter(tipo='CASAL')
    context['dados_quarto'] = dados_quarto
    return render(request, 'casal.html', context) #retorna a pagina casal.html

# ----------------------------------------------------------------------------------------------------------------------------

# Função que retorna a pagina comfort.html, onde aparece os quartos do tipo conforto

def comfort(request):
    context = {}
    dados_quarto = quarto.objects.filter(tipo='CONFORTO')
    context['dados_quarto'] = dados_quarto
    return render(request, 'comfort.html', context) #retorna a pagina comfort.html

# ----------------------------------------------------------------------------------------------------------------------------

# Função que retorna a pagina luxo.html, onde aparece os quartos do tipo luxo

def luxo(request):
    context = {}
    dados_quarto = quarto.objects.filter(tipo='LUXO')
    context['dados_quarto'] = dados_quarto
    return render(request, 'luxo.html', context) #retorna a pagina luxo.html

# ----------------------------------------------------------------------------------------------------------------------------

# Função que retorna a pagina nome.html, onde o usuario pode se cadastrar

def nome(request): #cadastro de usuario
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_usuario = form.cleaned_data['usuario']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['senha']

            user = User.objects.create_user(username=var_usuario, email=var_email, password=var_senha)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()

            print(var_first_name)
            print(var_last_name)
            print(var_usuario)
            print(var_email)
            print(var_senha)

            return HttpResponse("<h1>thanks</h1>")
    else:
        form = FormNome()

        return render(request, "nome.html", {"form": form})
    
# ----------------------------------------------------------------------------------------------------------------------------

# Função que retorna a pagina reservar_quarto.html, onde o usuario pode reservar um quarto
    
def reservar_quarto(request):
    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_data = form.cleaned_data['data']
            var_quarto = form.cleaned_data['quarto']

            reservar_quarto = Reserva_quarto(nome=var_nome, email=var_email, idade=var_idade, data=var_data, quarto=var_quarto)
            reservar_quarto.save()

            print(var_nome)
            print(var_email)
            print(var_idade)
            print(var_data)
            print(var_quarto)

            return render(request, "reserva_sucesso.html")
    else:
        form = FormReserva()

        return render(request, "reservar_quarto.html", {"form": form})
    
# ----------------------------------------------------------------------------------------------------------------------------
    
def reserva_sucesso(request):
    return render(request, "reserva_sucesso.html") #retorna a pagina reserva_sucesso.html

# ----------------------------------------------------------------------------------------------------------------------------

# Função que retorna a pagina login.html, onde o usuario pode fazer login

def login(request):
    form = FormLogin(request.POST)
    if form.is_valid():
        var_usuario = form.cleaned_data['usuario']
        var_senha = form.cleaned_data['senha']

        user = authenticate(username=var_usuario, password=var_senha)

        if user is not None:
            login(request, user)
            return HttpResponse("<h1>Logado com sucesso</h1>")
        else:
            return HttpResponse("<h1>Usuário ou senha inválidos</h1>")
        
    return render(request, "login.html", {"form": form}) #retorna a pagina login.html

# ----------------------------------------------------------------------------------------------------------------------------
