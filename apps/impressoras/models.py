from django.db import models
from categorias.models import Categoria

# Create your models here.

from django.db import models

class Categoria(models.Model): 
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Impressora(models.Model):
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)
    preco = models.DecimalField('Preço por dia', max_digits=10, decimal_places=2)
    
    STATUS_CHOICES = [
        ('em_uso', 'Em uso'),
        ('disponivel', 'Disponível'),
    ]
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='disponivel')

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    class Meta:
        verbose_name = 'Impressora'
        verbose_name_plural = 'Impressoras'
        ordering = ['id']

    def __str__(self):
        return f"{self.marca} {self.modelo}"
