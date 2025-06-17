from django.db import models

class Cliente(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', max_length=100, unique=True)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    phone = models.CharField('Telefone', max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.name

       #class Cliente {
  #  - nome: String
    #- email: String
    #- cpf: String
  #  - telefone: String
  #  --
   # + toString(): String
#}
