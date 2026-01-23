from django.forms import ValidationError
from django import forms
from .models import Thread, Post


FORBIDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа',
                  'дешево', 'бесплатно','біржа','робота',
                  'робота в інтернеті', 'реклама']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("Повідомлення повинно містити щонайменше 10 символів")
        
        for word in FORBIDEN_WORDS:
            if word in content.lower():
                raise ValidationError(f"Ваше повідомллення містить заборонене слово: {word}")
            
        if content.count('http') > 2:
            raise ValidationError("Занадто багато покликань. Максимум 2")
        
        return content
    
