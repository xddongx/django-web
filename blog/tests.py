from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post, Comment
from django.utils import timezone
from bs4 import BeautifulSoup


def create_post(title, content, author):
    blog_post = Post.objects.create(
        title = title,
        content = content,
        created = timezone.now(),
        author = author
    )

    return blog_post

def create_comment(post, text='a comment', author=None):
    if author is None:
        author, is_created=User.objects.get_or_create(
            username='guest',
            password='guestpassword'
        )
    comment = Comment.objects.create(
        post = post,
        text = text,
        author = author
    )

    return comment

class TestModel(TestCase):
    def setUp(self):
        self.client = Client()
        self.author_000 =User.objects.create_user(username='ddong', password='ddong')

    def test_post(self):
        post_000 = create_post(
            title='first title',
            content='first content',
            author=self.author_000
        )

    def test_comment(self):
        post_000 = create_post(
            title='first title',
            content='first content',
            author=self.author_000
        )

        self.assertEqual(Comment.objects.count(), 0)

        comment_000 = create_comment(
            post=post_000
        )

        comment_001 = create_comment(
            post = post_000,
            text = 'second comment'
        )

        self.assertEqual(Comment.objects.count(), 2)



class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.author_000 = User.objects.create_user(username='ddong', password='ddong')

    def refresh(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def test_none_post(self):
        soup = self.refresh('/blog/')

        body = soup.text
        title = soup.title
        self.assertIn(title.text, 'Blog')

        self.assertEqual(Post.objects.count(), 0)
        self.assertIn('아직 게시글이 없습니다.', body)

    def test_post_list(self):
        post_000 = create_post(
            title='first title',
            content='first content',
            author=self.author_000
        )

        soup = self.refresh('/blog/')

        body = soup.text
        title = soup.title
        self.assertIn('first title', body)

    def test_post_detail(self):
        post_000 = create_post(
            title='first title',
            content='first content',
            author=self.author_000
        )

        post_000_url = post_000.get_absolute_url()
        self.assertEqual(post_000_url, '/blog/{}/'.format(post_000.pk))

        soup = self.refresh(post_000_url)




