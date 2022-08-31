from django import forms

from .models import Record, Text


class RecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ('watch', 'duty_time', 'pub_date', 'on_work',)
        
        labels = {
            'pub_date': 'Дата',
            'watch': 'Вахта №',
            'duty_time': 'Смена',
            'on_work': 'Приемка смены',
        }
        help_texts = {
            'pub_date': 'Введите дату',
            'watch': 'Введите номер вахты',
            'duty_time': 'Введите смену',
            'on_work': 'Введите состояние на приемку смены',
        }
        verbose_name = 'Форма события смены'
        
class TextForm(forms.ModelForm):
    
    class Meta:
        model = Text
        fields = ('pub_time', 'text',)
        
        labels = {
            'pub_time': 'Время',
            'text': 'Событие',
        }
        help_texts = {
            'pub_time': 'Введите время события',
            'text': 'Введите событие',
        }
        verbose_name = 'Форма события смены'
        
        
