from django.forms import DateInput, ModelForm

from .models import Apropriacao


class ApropriacaoForm(ModelForm):
    class Meta:
        model = Apropriacao
        fields = [
            'referenciaApropriacao', 'colaborador', 'projeto', 'horas',
            'descricao'
        ]
