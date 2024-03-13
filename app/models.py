from django.db import models
from django.contrib import admin
from app.models import *


class ManterPessoas(models.Model):
    LOCADOR = 'LOCADOR'
    LOCATARIO = 'LOCATARIO'
    AVALISTA = 'AVALISTA'

    TIPO_CHOICES = [
        (LOCADOR, 'Locador'),
        (LOCATARIO, 'Locatário'),
        (AVALISTA, 'Avalista'),
    ]

    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)  
    rg = models.CharField(max_length=20)  # Defina o comprimento do campo RG conforme necessário
    data_nasc = models.DateField()
    email = models.EmailField()
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()}) - {self.cpf} {self.rg} {self.data_nasc} {self.email} {self.cidade}"
    
class ManterCargos(models.Model):
    GERENTE = 'GERENTE'
    ASSISTENTE_ADM = 'ASSISTENTE ADM'

    TIPO_CHOICES = [
        (GERENTE, 'Gerente'),
        (ASSISTENTE_ADM, 'Assistente ADM'),
]

    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)    
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})" 

class Manter_Tipo_Logradouro(models.Model):
    AVENIDA = 'AVENIDA'
    RUA = 'RUA'
    ALAMEDA = 'ALAMEDA'
    VIELA = 'VIELA'

    TIPO_CHOICES = [
        (AVENIDA, 'Avenida'),
        (RUA, 'Rua'),
        (ALAMEDA, 'Alameda'),
        (VIELA, 'Viela')
]
    
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})" 

class Manter_Bairros(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Manter_Logradouros(models.Model):
    

