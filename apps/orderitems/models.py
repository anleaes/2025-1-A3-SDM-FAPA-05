from django.db import models
from printers.models import Printer
from orders.models import RentalOrder
# Create your models here.

class RentalItem(models.Model):
    quantity = models.PositiveIntegerField('Quantidade', null=True, blank=True, default=1)
    unitary_price = models.DecimalField('Preço Unitário', max_digits=10, decimal_places=2)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name='Impressora')
    rental_order = models.ForeignKey(RentalOrder, on_delete=models.CASCADE, related_name='itens', verbose_name='Pedido de Aluguel')

    class Meta:
        unique_together = ('rental_order', 'printer')
        verbose_name = 'Item de Aluguel'
        verbose_name_plural = 'Itens de Aluguel'
        ordering = ['id']

    def __str__(self):
        return f"{self.quantity}x {self.printer.name} no pedido #{self.rental_order.id}"