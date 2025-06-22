from django.db import models

# Create your models here.

class Itemaluguel(models.Model):
    name = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    quantidadedias = models.TextField('Quantidade de Dias', max_length=100)
    preco = models.TextField('Preço Total', max_length=100)
    obs = models.TextField('Observacoes', max_length=100)

    class Meta:
        verbose_name = 'Item so Aluguel'
        verbose_name_plural = 'Itens do Aluguel'
        ordering =['id']

    def __str__(self):
        return self.name
