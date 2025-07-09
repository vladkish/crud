from django.db import models
from django.contrib.auth.models import AbstractUser

# Main user.
class User(AbstractUser):
    image = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/author.jpg')
    about_me = models.TextField(null=True, blank=True)