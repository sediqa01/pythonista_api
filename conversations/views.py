from rest_framework import generics, permissions
from pythonista_api.permissions import IsOwnerOrReadOnly
from .models import Conversation
from .serializers import ConversationSerializer, ConversationDetailSerializer


class ConversationList(generics.ListCreateAPIView):
    """
    List all Conversation
    Create a new Conversation if authenticated
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a Conversation, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ConversationDetailSerializer
    queryset = Conversation.objects.all()