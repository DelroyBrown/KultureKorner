from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'KultureKorner_base'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KultureKorner_home.urls')),
    path('', include('KultureKorner_postArt.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
