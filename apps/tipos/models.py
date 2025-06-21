from django.db import models
from tipos.models import Tipo  

# Create your models here.

class Impressora(models.Model):
    nome = models.CharField('Nome', max_length=50)
    marca = models.CharField('Marca', max_length=50)
    preco_diario = models.DecimalField('Preço Diário', max_digits=8, decimal_places=2)
    status = models.CharField('Status', max_length=20)
    modelo = models.CharField('Modelo', max_length=50)

    class Meta:
        verbose_name = 'Impressora'
        verbose_name_plural = 'Impressoras'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} - {self.marca} ({self.modelo})'
