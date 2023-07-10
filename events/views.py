from rest_framework import generics, permissions, filters
from pythonista_api.permissions import IsOwnerOrReadOnly
from .models import Event
from django.db.models import Count
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    List all Events
    Create a new Events if authenticated
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.annotate(
        conversations_count=Count('conversation', distinct=True),
        joins_count=Count('joins', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]

    ordering_fields = [
        'conversations_count',
        'joins_count',
        'joins__created_at',
        'event_date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a Events, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.annotate(
        conversations_count=Count('conversation', distinct=True),
        joins_count=Count('joins', distinct=True),
    ).order_by('-created_at')