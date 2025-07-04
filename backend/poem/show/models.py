from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.title}'
    
class Poem(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='poems')
    date_public = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}, {self.text} == {self.category}'