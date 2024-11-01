from django.contrib import admin
from .models import Registros

class RegistrosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nome_mae', 'data_nascimento', 'numero_caixa']
    list_filter = ['numero_caixa']
    search_fields = ['nome']

admin.site.register(Registros, RegistrosAdmin)