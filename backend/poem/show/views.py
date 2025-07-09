from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Poem, Comment, SavePoem
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def index(request, category_id=None):

    context = {
        'categoryies' : Category.objects.all(),
        'last_poem' : Poem.objects.filter(category_id=category_id) if category_id else Poem.objects.all().order_by('-id')[:3],
        'title' : Category.objects.get(id=category_id) if category_id else "Посдение посты"
    }
    
    return render(request, 'show/index.html', context)

def poem(request, poem_id):
    
    poem = Poem.objects.get(id=poem_id)
    
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                comment.user = request.user
            except:
                return redirect('users:login')
            comment.poem = Poem.objects.get(id=poem_id)
            comment.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = CommentForm()
    
    context = {
        'poem' : poem,
        'form' : form,
        'comments' : Comment.objects.filter(poem_id=poem_id),
    }
    
    poem.reads.add(request.user)
    
    return render(request, 'show/poem.html', context)

# System likes.
@login_required
def like(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    context = {}
    if not request.user in poem.like.all():
        poem.like.add(request.user)
    else:
        poem.like.remove(request.user)
    return redirect(request.META['HTTP_REFERER'])

@login_required
def save_poem(request, poem_id):
    poem = get_object_or_404(Poem, id=poem_id)
    user = request.user
    
    if SavePoem.objects.filter(poem=poem, user=user).exists():
        return redirect(request.META['HTTP_REFERER'])
    else:
        # Create objects
        SavePoem.objects.create(poem=poem, user=user)
    return redirect(request.META['HTTP_REFERER'])