from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    
    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'title', 'description', 'location',
            'starts_at', 'ends_at','created_at',
             'updated_at', 'image', 'event_date',
            'is_owner', 'profile_id','profile_image',
        ]