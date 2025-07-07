from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User

class LoginForm(AuthenticationForm):
    pass

# Custom form
class SignForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Ваше имя' 
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : "Ваш email"
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : "Придумайте пароль"
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : "Повторите пароль"
    }))
        
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')