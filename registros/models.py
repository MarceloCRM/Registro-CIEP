from django.db import models

class Registros(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False)
    nome_mae = models.CharField('Nome da mãe', max_length=100, blank=False)
    data_nascimento = models.DateField('Data de nascimento', blank=False)
    numero_caixa = models.IntegerField('Número da caixa', blank=False)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'