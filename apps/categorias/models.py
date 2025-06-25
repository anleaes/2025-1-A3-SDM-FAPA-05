from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=200)
    codigo = models.CharField('Código', max_length=20, unique=True)
    ativa = models.BooleanField('Ativa', default=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name

