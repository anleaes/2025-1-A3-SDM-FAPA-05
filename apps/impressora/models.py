from django.db import models
from tipo.models import Category

# Create your models here.

class Impressora(models.Model):
    name = models.CharField('Nome', max_length=50)
    marca = models.CharField('Marca', max_length=50)
    precoDiario = models.DecimalField('Preço Diário', max_digits=10, decimal_places=2) 
    status = models.CharField('Status', max_length=20, choices=[('disponivel', 'Disponível'), ('indisponivel', 'Indisponível')], default='disponivel')
    class Meta:
        verbose_name = 'Impressora'
        verbose_name_plural = 'Impressoras'
        ordering =['id']

    def __str__(self):
        return self.name
#Products - Impressora
#class Impressora {
   # - nome: String
   # - marca: String
   # - precoDiario: double
   # - status: String
   # --
   # + toString(): String
#}
