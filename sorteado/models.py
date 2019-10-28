from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    CHOICES = (
        ('PP', 'PP'), 
        ('P', 'P'), 
        ('M', 'M'), 
        ('G', 'G'), 
        ('GG', 'GG'), 
    )
    TAMANHO = (
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
    )
    SEXO = (
        ('Masculino', 'M'),
        ('Feminino', 'F')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_calcado = models.CharField('Número do calçado', max_length=2, choices=TAMANHO)
    tamanho_saia = models.IntegerField('Tamanho da saia (Caso seja uma mulher)', blank=True, null=True)
    tamanho_blusa = models.CharField('Tamanho da camisa ou blusa', max_length=2, blank=True, null=True, choices=CHOICES)
    sexo = models.CharField('Sexo', max_length=100, choices=SEXO)
    amigo_secreto = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT, related_name='user')    

    def __str__(self):
        return self.user.first_name
