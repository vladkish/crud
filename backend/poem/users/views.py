from django.shortcuts import render, redirect
from .forms import LoginForm, SignForm, ProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from show.models import SavePoem

def login(request):
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            
            if user:
                auth.login(request, user)
                
                messages.success(request, 'Успешно вошли!')
                return redirect('index')
    else:
        form = LoginForm()    
        
    context = {
        'form' : form
    }           
    
    return render(request, 'users/login.html', context)

def sign(request):
    
    if request.method == "POST":
        form = SignForm(data=request.POST)
        email = request.POST['email']
        
        if form.email_checking(email):
            if form.is_valid():
                user = form.save()
                auth.login(request, user)
                
                messages.success(request, 'Успешно создали!')
                return redirect('index')
            else:
                messages.error(request, 'Неправильные данные')
        else:
            messages.error(request, 'Почта уже занята :(')
    else:
        form = SignForm()
        
    context = {
        'form' : form
    }
    
    return render(request, 'users/sign.html', context)

@login_required
def profile(request):
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=request.user)
        
    context = {
        'form' : form,
        'save_poems' : SavePoem.objects.filter(user=request.user)
    }
    
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    
    messages.success(request, 'Вышли!')
    return redirect('index')