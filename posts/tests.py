from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post


class PostListViewTests(APITestCase):
    """
    Posts Detail view Test
    """
    def setUp(self):
        User.objects.create_user(username='developer', password='django.rf')

    def test_can_list_posts(self):
        developer = User.objects.get(username='developer')
        Post.objects.create(owner=developer, content='new post')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='developer', password='django.rf')
        response = self.client.post(
            '/posts/', {'content': 'pythonista post content'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_can_not_create_post(self):
        response = self.client.post(
            '/posts/', {'content': 'pythonista post content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
