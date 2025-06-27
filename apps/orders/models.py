from django.db import models
from clients.models import Client
from printers.models import Printer

# Create your models here.

class RentalOrder(models.Model):
    payment_method = models.CharField('Forma de Pagamento', max_length=30, choices=[
        ('boleto', 'Boleto'),
        ('cartao', 'Cartão de Crédito'),
        ('pix', 'PIX'),
    ])
    status = models.CharField('Status', max_length=20, default='pendente', choices=[
        ('pendente', 'Pendente'),
        ('ativo', 'Aluguel Ativo'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ])
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name='Impressora')
    start_date = models.DateField('Data de Início')
    end_date = models.DateField('Data de Término', null=True, blank=True)

    class Meta:
        verbose_name = 'Pedido de Aluguel'
        verbose_name_plural = 'Pedidos de Aluguel'
        ordering = ['id']

    def __str__(self):
        return f"Aluguel de {self.printer} por {self.client}"