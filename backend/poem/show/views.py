from django.shortcuts import render

def index(request):
    return render(request, 'show/index.html')

def poem(request):
    return render(request, 'show/poem.html')