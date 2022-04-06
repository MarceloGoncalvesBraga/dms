
from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse_lazy ,include,re_path,path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # GET /
    path('', include('jogos.urls', namespace='jogos')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
