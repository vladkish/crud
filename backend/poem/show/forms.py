from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    text = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Введите сообщение'
    }))
    
    class Meta:
        model = Comment
        fields = ('text', )