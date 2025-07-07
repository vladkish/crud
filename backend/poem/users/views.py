from django.shortcuts import render, redirect
from .forms import LoginForm, SignForm, ProfileForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            
            if user:
                auth.login(request, user)
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
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('index')
        else:
            print(form.errors)
        
    context = {
        'form' : form
    }
    
    return render(request, 'users/sign.html', context)

@login_required
def profile(request):
    
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=request.user)
        
    context = {
        'form' : form
    }
    
    return render(request, 'users/profile.html', context)