from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Profile


class ProfileListViewTests(APITestCase):
    """
    Profile model list view tests
    """
    def setUp(self):
        User.objects.create_user(
            username='pythonista', password='pp5.react')
        User.objects.create_user(
            username='developer', password='django.rf')

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_created_on_user_creation(self):
        self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 2)
