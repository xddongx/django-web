from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm


class PostList(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-created')


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self),  self).get_context_data(**kwargs)
        context['comment_form']=CommentForm()

        return context

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title', 'content', 'head_image'
    ]

    def form_valid(self, form):
        current_user = self.request.user  # 현재 이것을 작동시키는 user를 가져온다
        if current_user.is_authenticated:
            form.instance.author = current_user  # author를 current_user로 자동으로 채워줘라
            return super(type(self), self).form_valid(form)
        else:
            return redirect('/blog/')

class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title', 'content', 'head_image'
    ]


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)

    if request.user == post.author:
        post.delete()
        return redirect('/blog/')
    else:
        raise PermissionError('Post 삭제 권한이 없습니다.')

@require_POST
def new_comment(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid(): # comment_form이 유효한 경우에
            comment = comment_form.save(commit=False) # post랑 author를 채워줘야 하기 때문에 지금 가져온 것엔 text뿐이다
            comment.post = post
            comment.author = request.user # 지금 사용하고있는 user
            comment.save() # 세개를 다 채웠으니 저장해도 된다
            return redirect(post.get_absolute_url())
    else:
        return redirect('/blog/')