from django.urls import path
from . import views

app_name = 'show'

urlpatterns = [
    path('poem/<int:poem_id>/', views.poem, name="poem")
]