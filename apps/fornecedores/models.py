from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    razao_social = models.CharField('Razão Social', max_length=100)
    nome = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')
    endereco = models.CharField('Endereço', max_length=200)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['id']

    def __str__(self):
        return self.nome