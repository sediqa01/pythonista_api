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

    def test_logged_out_user_can_not_create_conversation(self):
        event_first = Event.objects.get(id=1)
        response = self.client.post(
            '/conversations/', {
                'event': event_first, 'content': 'a new content'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Conversation.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_add_conversation(self):
        self.client.login(username='pythonista', password='pp5.react')
        event_first = Event.objects.get(id=1)
        current_user = User.objects.get(username='pythonista')
        response = self.client.post(
            '/conversations/', {
                'owner': current_user, 'event': 1, 'content': 'a new content'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)