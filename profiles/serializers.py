from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

        """
        Checks if the requested user is the same as the owner.
        """
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

         

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'full_name', 'bio', 'created_at', 'updated_at',
            'github', 'linkedin', 'website', 'stack_overflow', 'image', 'is_owner'
        ]
