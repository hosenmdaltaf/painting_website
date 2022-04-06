
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',include('homeapp.urls')),
    path('blog/',include('blogapp.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    #urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


