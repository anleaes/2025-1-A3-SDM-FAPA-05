from django.db import models

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', max_length=100)
    tipo = models.CharField('Tipo de Impressora', max_length=50)
    uso_indicado = models.CharField('Uso Indicado', max_length=100)
    colorida = models.BooleanField('Impressão Colorida?', default=True)
    velocidade_media_ppm = models.PositiveIntegerField(
        'Velocidade Média (páginas por minuto)',
        null=True,
        blank=True
    )
    resolucao = models.CharField(
        'Resolução Máxima',
        max_length=50,
        help_text='Ex: 1200x1200 dpi',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.name
