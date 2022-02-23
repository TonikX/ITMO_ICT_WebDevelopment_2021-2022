from djoser.serializers import UserCreateSerializer


# Переопределяем сериализатор регистрации из Djoser и добавляем имя и фамилию
class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ("username", "first_name", "last_name", "password")
