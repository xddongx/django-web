from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')
