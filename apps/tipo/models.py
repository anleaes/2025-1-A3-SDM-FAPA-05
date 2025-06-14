from django.db import models

# Create your models here.

class Tipo(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    velocidade = models.IntegerField('Velocidade')
    resolucao = models.CharField('Resolucao', max_length=20, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering =['id']

    def __str__(self):
        return self.name
    
    #class Tipo {
   # - nome: String
   # - descricao: String
   # - velocidade: int
   # - resolucao: String
   # --
   # + toString(): String
