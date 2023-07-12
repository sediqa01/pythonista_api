from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post
from .models import Like


class LikeListViewTests(APITestCase):
    """
    Like list view Test
    """
    def setUp(self):
        pythonista = User.objects.create_user(
            username='pythonista', password='pp5.react')
        Post.objects.create(
            owner=pythonista, content='Coding is fun!')

    def test_can_list_all_joins(self):
        pythonista = User.objects.get(username='pythonista')
        post_first = Post.objects.get(id=1)
        Like.objects.create(owner=pythonista, post=post_first)
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_can_not_create_like(self):
        post_first = Post.objects.get(id=1)
        response = self.client.post('/likes/', {'post': post_first})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Like.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_add_like(self):
        self.client.login(username='pythonista', password='pp5.react')
        Post.objects.get(id=1)
        user = User.objects.get(username='pythonista')
        response = self.client.post(
            '/likes/', {'owner': user, 'post': 1}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)