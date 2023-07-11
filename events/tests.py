from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase


class EventListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='pythonista', password='pp5.react')

    def test_can_list_events(self):
        pythonista = User.objects.get(username='pythonista')
        Event.objects.create(
            owner=pythonista, title='a title', event_date='2023-07-22')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    

   