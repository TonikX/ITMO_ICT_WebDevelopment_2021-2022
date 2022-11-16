from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'avatar_url'
        )

    username = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    avatar_url = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_avatar_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.avatar_url)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'avatar_url', 'check_scan_token'
        )

    username = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    avatar_url = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_avatar_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.avatar_url)


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'avatar', 'avatar_url'
        )

    avatar_url = serializers.SerializerMethodField()

    def get_avatar_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.avatar_url)
