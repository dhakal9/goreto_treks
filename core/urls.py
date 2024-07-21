"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from django.urls import reverse
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
# from django.conf.urls import handler400, handler403, handler404, handler500
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path('admin/', admin.site.urls),
    re_path('', include('home.urls')),
    re_path('', include('tour.urls')),
    re_path('summernote/', include('django_summernote.urls')),
    re_path('tinymce/', include('tinymce.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=serve, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'
handler403 = 'home.views.error_403'
handler400 = 'home.views.error_400'