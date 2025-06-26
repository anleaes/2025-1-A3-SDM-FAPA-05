from django.db import models
from categories.models import Category

class Printer(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao')
    is_active = models.BooleanField('Ativo', default=False)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)  # String com app.Model

    class Meta:
        verbose_name = 'Impressora'
        verbose_name_plural = 'Impressoras'
        ordering = ['id']

    def __str__(self):
        return self.name
