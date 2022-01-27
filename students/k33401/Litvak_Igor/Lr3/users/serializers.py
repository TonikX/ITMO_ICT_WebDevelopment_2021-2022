from djoser.serializers import UserCreateSerializer


class CustomUserCreateSerializer(UserCreateSerializer):
    """Require first_name and last_name for Djoser registration"""

    class Meta(UserCreateSerializer.Meta):
        fields = ["username", "first_name", "last_name", "password"]
