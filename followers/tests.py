from django.contrib.auth.models import User
from .models import Follower
from rest_framework import status
from rest_framework.test import APITestCase


class FollowerListViewTests(APITestCase):
    """
    Tests for the Follower model list view
    """
    def setUp(self):
        pythonista = User.objects.create_user(
            username='pythonista', password='pp5.react')
        developer = User.objects.create_user(
            username='developer', password='django.rf')
        programmer = User.objects.create_user(
            username='programmer', password='react.js')
        Follower.objects.create(owner=pythonista, followed=developer)
        Follower.objects.create(owner=pythonista, followed=programmer)

    def test_can_view_follower_list(self):
        User.objects.get(username='pythonista')
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_follow(self):
        self.client.login(username='developer', password='django.rf')
        response = self.client.post(
            '/followers/', {'owner': 2, 'followed': 3}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_can_not_follow(self):
        developer = User.objects.get(username='developer')
        programmer = User.objects.get(username='programmer')
        response = self.client.post(
            '/followers/', {'owner': developer, 'followed': programmer}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Follower.objects.count()
        self.assertEqual(count, 2)
