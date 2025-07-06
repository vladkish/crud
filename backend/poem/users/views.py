from django.shortcuts import render

def login(request):
    return render(request, 'users/login.html')

def sign(request):
    return render(request, 'users/sign.html')

def profile(request):
    return render(request, 'users/profile.html')