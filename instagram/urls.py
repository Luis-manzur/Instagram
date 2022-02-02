#Django
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #posts
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    
    #users
    path('users/', include(('users.urls', 'users'), namespace='users')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
