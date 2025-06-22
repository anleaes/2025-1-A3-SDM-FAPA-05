from django.db import models
from tipos.models import Tipo

# Create your models here.

class Impressora(models.Model):
    name = models.CharField('Nome', max_length=50)
    marca = models.TextField('Marca', max_length=100)
    preco_diario = models.DateField('Preco Diario', auto_now=False, auto_now_add=False) 
    status = models.BooleanField('Ativo', default=False)
    modelo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Impressora'
        verbose_name_plural = 'Impressoras'
        ordering =['id']

    def __str__(self):
        return self.name