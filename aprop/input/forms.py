from bootstrap_datepicker_plus import DatePickerInput
from django.forms import DateInput, ModelForm

from .models import Apropriacao


class ApropriacaoForm(ModelForm):
    class Meta:
        model = Apropriacao
        fields = [
            'referencia', 'projeto', 'duracao',
            'descricao'
        ]
