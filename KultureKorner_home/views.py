# KultureKorner_home/views.py
from django.shortcuts import render
from KultureKorner_postArt.models import PostArt


def home(request):
    posts = PostArt.objects.all().order_by("post_date")
    return render(request, "home/home.html", {"posts": posts})
