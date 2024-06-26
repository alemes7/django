from django.db import models
from django.utils import timezone

# Create your models here.

TIPOS__QUARTOS = (
    ("SOLTEIRO" , "Solteiro"),
    ("CASAL" , "Casal"),
    ("CONFORTO" , "Conforto"),
    ("LUXO" , "Luxo")
)

# Classe Hotel, onde é criado o modelo Hotel

class Hotel(models.Model):
    titulo = models.CharField(max_length=50) #models.CharField, é um tipo de dado que aceita strings
    descricao = models.TextField(max_length=500) #models.TextField, é um tipo de dado que aceita textos
    logo = models.ImageField(upload_to='logo/') #models.ImageField, é um tipo de dado que aceita imagens

    def __str__(self):
        return self.titulo
    
# ----------------------------------------------------------------------------------------------------------------------------

# Classe quarto, onde é criado o modelo quarto

class quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPOS__QUARTOS) #models.CharField, é um tipo de dado que aceita strings
    disponibilidade = models.IntegerField() #models.IntegerField, é um tipo de dado que aceita numeros inteiros
    valor = models.FloatField(max_length=4) #models.FloatField, é um tipo de dado que aceita numeros decimais
    descricao = models.TextField(max_length=255) #models.TextField, é um tipo de dado que aceita textos
    foto_quarto = models.ImageField(upload_to='foto_quartos/') #models.ImageField, é um tipo de dado que aceita imagens

    def __str__(self):
        return self.tipo
    
# ----------------------------------------------------------------------------------------------------------------------------

# Classe Reserva_quarto, onde é criado o modelo Reserva_quarto
    
class Reserva_quarto(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idade = models.IntegerField()
    data = models.DateField(default=timezone.now)
    quarto = models.CharField(max_length=50)

    def __str__(self):
        return self.nome # retorna o nome do cliente
# ----------------------------------------------------------------------------------------------------------------------------