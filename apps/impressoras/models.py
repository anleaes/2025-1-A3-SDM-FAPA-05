from categorias.models import Categoria

class Impressora(models.Model):
    name = models.CharField('Nome', max_length=50)
    marca = models.TextField('Marca', max_length=50)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    disponivel = models.BooleanField('Disponivel', default=False)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Impressora'
        verbose_name_plural = 'Impressoras'
        ordering =['id']

    def __str__(self):
        return self.name