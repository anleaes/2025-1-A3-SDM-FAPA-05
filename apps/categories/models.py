from django.db import models

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    uso_indicado = models.CharField('Uso Indicado', max_length=50, help_text='Ex: Doméstico, Empresarial, Gráfica')
   
    velocidade_media = models.PositiveIntegerField(
        'Velocidade Média (ppm)',
        help_text='Páginas por minuto',
        null=True,
        blank=True
    )
    tipo = models.CharField(
        'Tipo de Impressora',
        max_length=30,
        choices=[
            ('Laser', 'Laser'),
            ('Jato de Tinta', 'Jato de Tinta'),
            ('Térmica', 'Térmica'),
            ('Matricial', 'Matricial'),
            ('Multifuncional', 'Multifuncional'),
        ]
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name