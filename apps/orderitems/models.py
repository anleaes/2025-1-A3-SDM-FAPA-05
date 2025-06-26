from django.db import models
from products.models import Printer
from orders.models import Order
# Create your models here.


class Orderitem(models.Model):
   quantity = models.PositiveIntegerField('Quantidade', default=1)  # quantidade de impressoras alugadas
    rental_price_per_day = models.DecimalField('Preço de aluguel por dia', max_digits=10, decimal_places=2)
    printer = models.ForeignKey('Printer', on_delete=models.CASCADE)  # produto -> impressora
    order = models.ForeignKey('RentalOrder', on_delete=models.CASCADE)  # pedido/aluguel
    start_date = models.DateField('Data de início do aluguel')
    end_date = models.DateField('Data de fim do aluguel')

    class Meta:
        unique_together = ('order', 'printer')
        verbose_name = 'Item de aluguel'
        verbose_name_plural = 'Itens de aluguel'
        ordering = ['id']

    def __str__(self):
        return f"{self.quantity}x {self.printer.name} - {self.start_date} a {self.end_date}"
    
    def total_price(self):
        days = (self.end_date - self.start_date).days + 1
        return self.quantity * self.rental_price_per_day * days