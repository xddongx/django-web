from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    posts = Post.objects.all()
    return render(
        request,
        'basecamp/index.html/',
        {'posts': posts}
    )