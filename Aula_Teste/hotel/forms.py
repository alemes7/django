from django import forms

class nome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20)