from django import forms
from .models import quarto
from django.contrib.auth.models import User


class FormReserva(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20)
    email = forms.EmailField(label='Email', max_length=50)
    idade = forms.IntegerField(label='Idade')
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    quarto = forms.ModelChoiceField(label='Quarto', queryset=quarto.objects.filter(id__in=[1, 2, 3, 4]))

class FormCadastro(forms.Form):
    first_name = forms.CharField(label='Nome', max_length=20)
    last_name = forms.CharField(label='Sobrenome', max_length=20)
    email = forms.EmailField(label='Email', max_length=50)
    usuario = forms.CharField(label='Usuário', max_length=20)
    senha = forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput)

class FormLogin(forms.Form):
    usuario = forms.CharField(label='Usuário', max_length=20)
    senha = forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput)

class Profile(forms.ModelForm):
    class Meta: # class meta é uma classe interna que fornece metadados adicionais ao formulário
        model = User  # Especifica o modelo ao qual o formulário está vinculado
        fields = ['first_name', 'last_name', 'email']  # Especifica os campos do modelo a serem incluídos no formulário