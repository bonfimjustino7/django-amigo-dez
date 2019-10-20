from django.contrib import admin
from .models import *


class UsuarioAdmin(admin.ModelAdmin):
    list_display  = ('user', 'num_calcado', 'tamanho_saia', 'tamanho_blusa', 'amigo_secreto')
    readonly_fields = ('amigo_secreto',)

admin.site.register(Usuario, UsuarioAdmin)