from django.db import models
from users.models import User

# from time, for fnc date_count
from datetime import datetime
import time

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

    def plural_day(n):
        if 11 <= n % 100 <= 14:
            return 'дней'
        if n % 10 == 1:
            return 'день'
        elif 2 <= n % 10 <= 4:
            return 'дня'
        else:
            return 'дней'

    def plural_month(n):
        if 11 <= n % 100 <= 14:
            return 'месяцев'
        if n % 10 == 1:
            return 'месяц'
        elif 2 <= n % 10 <= 4:
            return 'месяца'
        else:
            return 'месяцев'

    def plural_year(n):
        if 11 <= n % 100 <= 14:
            return 'лет'
        if n % 10 == 1:
            return 'год'
        elif 2 <= n % 10 <= 4:
            return 'года'
        else:
            return 'лет'

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

        
class Comment(models.Model):
    user = models.ForeignKey(to=User, related_name='comment', on_delete=models.CASCADE)
    poem = models.ForeignKey(to=Poem, related_name='comment', on_delete=models.CASCADE)
    date_public = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    
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

    def plural_day(n):
        if 11 <= n % 100 <= 14:
            return 'дней'
        if n % 10 == 1:
            return 'день'
        elif 2 <= n % 10 <= 4:
            return 'дня'
        else:
            return 'дней'

    def plural_month(n):
        if 11 <= n % 100 <= 14:
            return 'месяцев'
        if n % 10 == 1:
            return 'месяц'
        elif 2 <= n % 10 <= 4:
            return 'месяца'
        else:
            return 'месяцев'

    def plural_year(n):
        if 11 <= n % 100 <= 14:
            return 'лет'
        if n % 10 == 1:
            return 'год'
        elif 2 <= n % 10 <= 4:
            return 'года'
        else:
            return 'лет'

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