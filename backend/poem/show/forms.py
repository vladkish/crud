from django import forms
from .models import Poem

class Comment(forms.ModelForm):
    
    text = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Введите сообщение'
    }))
    
    class Meta:
        model = Poem
        fields = ('text', 'user', 'poem')