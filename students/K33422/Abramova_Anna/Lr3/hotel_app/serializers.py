from rest_framework.serializers import ModelSerializer

from hotel_app.models import Admin, Room, Client, Inhabitation, Cleaner, Cleaning


class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class InhabitationSerializer(ModelSerializer):
    class Meta:
        model = Inhabitation
        fields = '__all__'


class CleanerSerializer(ModelSerializer):
    class Meta:
        model = Cleaner
        fields = '__all__'


class CleaningSerializer(ModelSerializer):
    class Meta:
        model = Cleaning
        fields = '__all__'

