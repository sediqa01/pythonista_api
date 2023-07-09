from rest_framework import serializers
from .models import Join


class JoinSerializer(serializers.ModelSerializer):
    """
    Join serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Join
        fields = [
            'id', 'owner', 'event', 'created_at'
        ]