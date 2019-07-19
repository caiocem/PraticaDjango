from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django.forms import ModelForm

from .models import Apropriacao


class ApropriacaoForm(ModelForm):
    class Meta:
        model = Apropriacao
        fields = ['referencia', 'projeto', 'duracao', 'descricao']
        widget = {
            'referencia':
            DatePickerInput(format='%Y-%m-%d',
                            options={
                                "showClose": True,
                                "showClear": False,
                                "showTodayButton": True,
                            }),
            'duracao':
            TimePickerInput(format='%H:%M',
                            attrs={'placeholder': '08:00'},
                            options={
                                "showClose": True,
                                "showClear": False,
                                "showTodayButton": False,
                                "stepping": 5,
                            })
        }
