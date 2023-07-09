from rest_framework import serializers
from .models import Conversation


class ConversationSerializer(serializers.ModelSerializer):
    """
    Conversation serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    
    class Meta:
        model = Conversation
        fields = [
            'id', 'event', 'content', 'created_at',
            'updated_at', 'owner','is_owner',
            'profile_id', 'profile_image',
        ]


class ConversationDetailSerializer(ConversationSerializer):
    """
    Serializer for the Conversation model used in Detail view.
    Conversation detail serializer inherits from ConversationSerializer,
    all its methods and attributes.
    """
    event = serializers.ReadOnlyField(source='event.id')