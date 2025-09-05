from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request, *args, **kwargs):
    return render(request, "home.html", {})


def interests(request, *args, **kwargs):
    return render(request, "interesting.html", {})