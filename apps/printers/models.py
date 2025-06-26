from django.db import models

# Create your models here.

class Printer(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Impressora'
        verbose_name_plural = 'Impressoras'
        ordering =['id']

    def __str__(self):
        return self.name
# from django.db import models
# from .models import Category  

# class Printer(models.Model):
#     name = models.CharField('Nome', max_length=50)
#     description = models.TextField('Descrição', max_length=100)
#     date_fabrication = models.DateField('Data de Fabricação')
#     is_active = models.BooleanField('Ativo', default=True)  # normalmente ativo começa como True
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')

#     class Meta:
#         verbose_name = 'Impressora'
#         verbose_name_plural = 'Impressoras'
#         ordering = ['id']

#     def __str__(self):
#         return self.name
