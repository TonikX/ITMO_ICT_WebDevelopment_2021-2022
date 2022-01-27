from rest_framework import serializers

from users.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'profile_picture',
            'bonus_count',
            'bookings_count'
        )
        read_only_fields = (
            'bonus_count',
        )
