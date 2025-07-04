from django.contrib import admin
from .models import Category, Poem

admin.site.register([Category, Poem])