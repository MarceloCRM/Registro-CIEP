from django import forms
from django.forms import TextInput, NumberInput
from .models import Registros

class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        fields = ["nome", "nome_mae", "data_nascimento", "numero_caixa"]
        widgets = {
            'nome': TextInput(attrs={'class':'input'}),
            'nome_mae': TextInput(attrs={'class':'input'}),
            'data_nascimento': TextInput(attrs={'class':'input'}),
            'numero_caixa': NumberInput(attrs={'class':'input'})
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=200, required=False)