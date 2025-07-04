from django.shortcuts import render
from .models import Category, Poem

def index(request, category_id=None):
    
    context = {
        'categoryies' : Category.objects.all(),
        'last_poem' : Poem.objects.filter(category_id=category_id) if category_id else Poem.objects.all().order_by('-id')[:3]
    }
    
    return render(request, 'show/index.html', context)

def poem(request, poem_id):
    
    context = {
        'poem' : Poem.objects.get(id=poem_id)
    }
    
    return render(request, 'show/poem.html', context)