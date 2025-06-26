from django.db import models

# Create your models here.

class Documents(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('RG', 'RG'),
        ('CPF', 'CPF'),
        ('CNH', 'CNH'),
        ('PASSAPORTE', 'Passaporte'),
        ('TIT_ELEITOR', 'Título de Eleitor'),
        ('CTPS', 'Carteira de Trabalho'),
        ('OUTRO', 'Outro'),
    ]

    tipo = models.CharField('Tipo de Documento', max_length=20, choices=TIPO_DOCUMENTO_CHOICES)
    numero = models.CharField('Número', max_length=30)
    orgao_emissor = models.CharField('Órgão Emissor', max_length=50, blank=True, null=True)
    data_emissao = models.DateField('Data de Emissão', blank=True, null=True)
    validade = models.DateField('Validade', blank=True, null=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering =['id']

    def __str__(self):
        return f'{self.tipo} - {self.numero}'