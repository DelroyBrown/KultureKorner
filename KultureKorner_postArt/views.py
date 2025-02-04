from django.shortcuts import render, get_object_or_404
from .models import PostArt


def post_detail(request, post_id):
    post = get_object_or_404(PostArt, pk=post_id)
    return render(request, "posts/post_detail.html", {"post": post})
