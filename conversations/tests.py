from django.contrib.auth.models import User
from .models import Event
from .models import Conversation
from rest_framework import status
from rest_framework.test import APITestCase


class ConversationListViewTests(APITestCase):
    def setUp(self):
        pythonista = User.objects.create_user(username='pythonista', password='pp5.react')
        event_first = Event.objects.create(
            owner=pythonista, title='Coding Event', event_date='2023-07-23')

    def test_can_list_conversations(self):
        pythonista = User.objects.get(username='pythonista')
        event_first = Event.objects.get(id=1)
        Conversation.objects.create(
            owner=pythonista, event=event_first, content='New conversations'
        )
        response = self.client.get('/conversations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)