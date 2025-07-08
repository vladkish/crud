from django.contrib import admin
from .models import Category, Poem, Comment

admin.site.register([Category, Poem, Comment])