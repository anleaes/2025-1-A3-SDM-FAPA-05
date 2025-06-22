from django.db import models

from apps.impressoras.models import Impressora

# Create your models here.

class Client(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail',null=False, blank=False)
    cpf= models.CharField('cpf', max_length=50)
    cell_phone = models.CharField('Telefone celular', max_length=20)
    endereco = models.CharField('Endereco', max_length=200)   
    #avaliação = models.ManyToManyField(avaliação, verbose_name="Avaliação")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name
    


    

# class Avaliacao(models.Model):
#     cliente = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
#     impressora = models.ForeignKey(Impressora, on_delete=models.CASCADE, verbose_name='Impressora')
#     nota = models.IntegerField('Nota', choices=[(i, str(i)) for i in range(1, 6)])
#     comentario = models.TextField('Comentário')
#     data = models.DateTimeField('Data', auto_now_add=True)

#     class Meta:
#         verbose_name = 'Avaliação'
#         verbose_name_plural = 'Avaliações'
#         ordering = ['-data']

#     def __str__(self):
#         return f'{self.cliente.nome} - {self.impressora.modelo} - {self.nota}★'