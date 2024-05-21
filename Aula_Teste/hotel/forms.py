from django import forms
from .models import quarto


class FormReserva(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20)
    email = forms.EmailField(label='Email', max_length=50)
    idade = forms.IntegerField(label='Idade')
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    quarto = forms.ModelChoiceField(label='Quarto', queryset=quarto.objects.filter(id__in=[1, 2, 3, 4]))

class FormLogin(forms.Form):
    usuario = forms.CharField(label='Usuário', max_length=20)
    senha = forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput)