from django.db import models
from users.models import User

# from time, for fnc date_count
from datetime import datetime
import time

# Для создание списка в поле модели.
from django.db.models import JSONField

class Category(models.Model):
    title = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.title}'
    
class Poem(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='poems')
    date_public = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(to=User, related_name="poems", blank=True)
    reads = models.ManyToManyField(to=User, related_name="reads")
    
    def __str__(self):
        return f'{self.title}, {self.text} == {self.category}'

    def text_poem(self):
        dot = self.text.count('.')
        if dot > 1:
            total = self.text.find('.')
            total_str = self.text.find('.', total + 1)
            return f"{self.text[0:total_str + 1]}..."
        else:
            return self.text

    def date_count(self):
        now_date = self.date_public.date()
        today = datetime.today().date()

        delta = (today - now_date).days

        if delta == 0:
            return 'Сегодня'
        elif delta == 1:
            return 'Вчера'
        elif delta == 7:
            return 'Неделю назад'
        elif delta < 31:
            return f'{delta} дней назад'
        elif delta < 365:
            months = delta // 30
            return f'{months} месяц(ев) назад'
        else:
            years = delta // 365
            return f'{years} год(а/лет) назад'
        

# Filter for Comments.
class BadWords(models.Model):
    bad_words = models.CharField(max_length=120)
    
    def __str__(self):
        return f'{self.bad_words}'
        

# Manager model Comment
class ManagerComment(models.QuerySet):
    def checking(self, username):
        self.total = []
        for word in list(self):
            
            # Save username in list.
            self.total.append(str(word).split()[0])
        
        answer = set(self.total)
        if len(answer) == 1 and self.total[0] == username:
            return False
        return True
            
        
class Comment(models.Model):
    user = models.ForeignKey(to=User, related_name='comment', on_delete=models.CASCADE)
    poem = models.ForeignKey(to=Poem, related_name='comment', on_delete=models.CASCADE)
    date_public = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)
    
    # Connect.
    objects = ManagerComment.as_manager()
    
    def __str__(self):
        return f'{self.user} for poem'
    
    def text_poem(self):
        dot = self.text.count('.')
        if dot > 1:
            total = self.text.find('.')
            total_str = self.text.find('.', total + 1)
            return f"{self.text[0:total_str + 1]}..."
        else:
            return self.text
        
    def filters(self, text):

        banned_words = BadWords.objects.values_list('bad_words', flat=True)
        
        text_lower = text.lower()
        
        for word in banned_words:
            if word and word.lower() in text_lower:
                return False
        return True
    
    def max_comments(self):
        if Comment.objects.all()[-4:]:
            pass

class SavePoem(models.Model):
    poem = models.ForeignKey(to=Poem, on_delete=models.CASCADE, related_name='save_poems')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='save_poems')
    
    def __str__(self):
        return f'{self.poem} for {self.user}'  