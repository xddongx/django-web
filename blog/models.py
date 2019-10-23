from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{} : {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)

    def get_update_url(self):
        return self.get_absolute_url() + 'update/'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    text = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)  # 새로 생성됬을때 저절로 시간이 들어가게
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return self.post.get_absolute_url()