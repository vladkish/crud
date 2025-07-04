from django.urls import path
from . import views

app_name = 'show'

urlpatterns = [
    path('poem/', views.poem, name="poem")
]