from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Poem, Comment, SavePoem
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.contrib import messages

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
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if not request.user.is_authenticated:
                
                messages.success(request, 'Для работы на сайте нужна Авторизация')
                return redirect('users:login')
            
            comment.user = request.user
            comment.poem = poem
            
            last_comment = poem.comment.order_by('-id')[:4]
        
            if last_comment.checking(request.user.username):
                if comment.filters(text=comment.text):
                    comment.save()
                else:
                    return messages.error(request, 'Вы не можете такое писать!')
            else:
                return messages.error(request, 'Вы не можете пока что писать!')

            return redirect(request.META.get('HTTP_REFERER', '/'))

        
    else:
        form = CommentForm()
    
    context = {
        'poem': poem,
        'form': form,
        'comments': reversed(Comment.objects.filter(poem_id=poem_id).order_by('-id')[:6]),
        'count_comment' : Comment.objects.filter(poem_id=poem_id).count(),
    }
    
    try:
        context['saved_poems'] = request.user.read_poems.all()[:3]
    except:
        context
    
    if request.user.is_authenticated:
        poem.reads.add(request.user)
        request.user.read_poems.add(poem)
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
    poem_obj = SavePoem.objects.filter(poem=poem, user=user)
    
    if poem_obj.exists():
        poem_obj.delete()
    else:
        # Create objects
        SavePoem.objects.create(poem=poem, user=user)
    return redirect(request.META['HTTP_REFERER'])