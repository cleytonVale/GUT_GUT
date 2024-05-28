from django import forms
from .models import Bebe, Alimentacao, TrocaDeFralda, Sono, ConsultaMedica

class BebeForm(forms.ModelForm):
    class Meta:
        model = Bebe
        fields = ['nome', 'data_nascimento', 'peso', 'altura', 'grupo_sanguineo']

class AlimentacaoForm(forms.ModelForm):
    class Meta:
        model = Alimentacao
        fields = ['bebe', 'data_hora', 'tipo', 'quantidade']

class TrocaDeFraldaForm(forms.ModelForm):
    class Meta:
        model = TrocaDeFralda
        fields = ['bebe', 'data_hora', 'tipo', 'observacoes']

class SonoForm(forms.ModelForm):
    class Meta:
        model = Sono
        fields = ['bebe', 'data_hora_inicio', 'data_hora_fim', 'qualidade']

class ConsultaMedicaForm(forms.ModelForm):
    class Meta:
        model = ConsultaMedica
        fields = ['bebe', 'data_hora', 'medico', 'motivo', 'observacoes']
