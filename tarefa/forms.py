from django import forms
from django.forms import fields
from .models import TarefaDb


class ConteudoForm(forms.ModelForm):
    class Meta:
        model = TarefaDb
        fields = ('conteudo',)

        