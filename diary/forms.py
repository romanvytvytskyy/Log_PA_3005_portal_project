from django import forms
from .models import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'value', 'comment']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 
                                              'min': 1, 'max': 12,
                                              'placeholder': 'Оцінка від 1 до 12'}),
            'comment':forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Коментар'}),
        }
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 1 or value > 12:
            raise forms.ValidationError("Оцінка повинна бути від 1 до 12")
        return value