from django.shortcuts import render
from .models import Category, Poem

def index(request):
    
    context = {
        'categoryies' : Category.objects.all(),
        'last_poem' : Poem.objects.all().order_by('-id')[:3]
    }
    
    return render(request, 'show/index.html', context)

def poem(request):
    return render(request, 'show/poem.html')