from django.db import models

class Tipo(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição')
    velocidade = models.IntegerField('Velocidade')
    resolucao = models.CharField('Resolução', max_length=50)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - {self.resolucao} ({self.velocidade} MHz)"
