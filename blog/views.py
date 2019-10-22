from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class PostList(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post
