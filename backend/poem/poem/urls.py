from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)