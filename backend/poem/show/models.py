from django.db import models
from users.models import User

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
    
    # Функция вывода правильного текста
    def text_poem(self):
        dot = self.text.count('.')
        if dot > 1:
            total = self.text.find('.')
            total_str = self.text.find('.', total + 1)
            return f"{self.text[0:total_str + 1]}..."
        else:
            return self.text
        
class Comment(models.Model):
    user = models.ForeignKey(to=User, related_name='comment', on_delete=models.CASCADE)
    poem = models.ForeignKey(to=Poem, related_name='comment', on_delete=models.CASCADE)
    date_public = models.DateTimeField(auto_now_add=True)
    text = models.TextField()