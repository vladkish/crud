from django.contrib import admin
from django.urls import path, include

from show import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # index
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.index, name='category'),
    
    # show app
    path('show/', include('show.urls', namespace="show")),
    
    # users app
    path('users/', include('users.urls', namespace="users"))
]
