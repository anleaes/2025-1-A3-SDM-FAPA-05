from django.db import models

class Category(models.Model):
    TIPO_IMPRESSORA_CHOICES = [
        ('laser', 'Laser'),
        ('jato_tinta', 'Jato de Tinta'),
        ('matricial', 'Matricial'),
        ('3d', '3D'),
        ('termo', 'Térmica'),
    ]

    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', max_length=100)
    tipo = models.CharField(
        'Tipo de Impressora',
        max_length=20,
        choices=TIPO_IMPRESSORA_CHOICES,
        default='laser'
    )
    colorida = models.BooleanField('Impressão Colorida?', default=True)
    velocidade_media_ppm = models.PositiveIntegerField(
        'Velocidade Média (páginas por minuto)',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.name
