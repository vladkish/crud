from django import forms
from .models import Poem

class Comment(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ('text', 'user', 'poem')