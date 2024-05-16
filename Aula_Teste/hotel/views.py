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
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'reserve.html', context) #retorna a pagina quartos.html

def solteiro(request):
    context = {}
    dados_quarto = quarto.objects.filter(tipo='SOLTEIRO')
    context['dados_quarto'] = dados_quarto
    return render(request, 'solteiro.html', context) #retorna a pagina solteiroo.html

def nome(request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']

            user = Usuario(nome=var_nome, email=var_email)
            user.save()

            print(var_nome)
            print(var_email)

            return HttpResponse("<h1>thanks</h1>")
    else:
        form = FormNome()

        return render(request, "nome.html", {"form": form})