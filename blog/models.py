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