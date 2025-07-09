from django.urls import path
from . import views

app_name = 'show'

urlpatterns = [
    path('poem/<int:poem_id>/', views.poem, name="poem"),
    
    # System likes.
    path('like/<int:poem_id>', views.like, name="like"),

    # Savepoem
    path('save/<int:poem_id>/', views.save_poem, name="save_poem")
]