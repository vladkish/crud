from django.contrib import admin
from .models import Category, Poem, Comment, BadWords

admin.site.register([Category, Poem, Comment, BadWords])