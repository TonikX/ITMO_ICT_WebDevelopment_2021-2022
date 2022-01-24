from rest_framework import serializers

from users.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'avatar_url', 'check_scan_token'
        )

    username = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    avatar_url = serializers.ReadOnlyField()


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'avatar',
        )
