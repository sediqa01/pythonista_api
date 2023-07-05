from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'full_name', 'bio', 'created_at', 'updated_at',
            'github', 'linkedin', 'website', 'stack_overflow', 'image'
        ]
