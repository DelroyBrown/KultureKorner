from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "KultureKorner_postArt"

urlpatterns = [
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
