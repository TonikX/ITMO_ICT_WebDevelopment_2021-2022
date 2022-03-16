from rest_framework import serializers
from .models import *


# Данные по работникам компании
class WorkerViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "fio", "age", "education", "stajh_raboty", "passport"


class WorkerCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    fio = serializers.CharField(max_length=100)
    age = serializers.IntegerField(default=18)
    education = serializers.ChoiceField(choices=Worker.education_types)
    stajh_raboty = serializers.IntegerField()
    passport = serializers.CharField(max_length=10)

    def create(self, validated_data):
        worker = Worker(**validated_data)
        worker.save()
        return Worker(**validated_data)


# Самолёты аэропорта
class PlaneViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = "__all__"


class PlaneCreateSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=15)
    number = serializers.CharField(max_length=8)
    mesta = serializers.IntegerField()
    speed = serializers.IntegerField()
    avia = serializers.CharField(max_length=20)

    def create(self, validated_data):
        services_pl = Plane(**validated_data)
        services_pl.save()
        return Plane(**validated_data)


# Посмотрим какие самолёты какой компании в каком количестве находятся в ремонте
class RemontDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remont
        fields = "__all__"

        depth = 1


class RemontViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remont
        fields = "__all__"


# Экипаж
class EkipazhViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ekipazh
        fields = "__all__"


# Утвердить должность в экипаже сотруднику авиакомпании
class AviacompanyNestedSerializer(serializers.ModelSerializer):
    id_ekipazha = EkipazhViewSerializer()
    id_workera = WorkerViewSerializer()

    class Meta:
        model = Aviacompany
        fields = "__all__"


class AviacompanyViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviacompany
        fields = "__all__"


class AviacompanyCreateSerializer(serializers.Serializer):
    id_ekipazha = serializers.PrimaryKeyRelatedField(queryset=Ekipazh.objects.all())
    id_workera = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all())

    work = serializers.CharField(max_length=30)

    def create(self, validated_data):
        aviacompany = Aviacompany(**validated_data)
        aviacompany.save()
        return Aviacompany(**validated_data)


# Пересадки
class TranzitViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tranzit
        fields = "__all__"


class TranzitCreateSerializer(serializers.ModelSerializer):
    punkt_peresadki = serializers.CharField(max_length=20)

    def create(self, validated_data):
        punkt_peresadki = Tranzit(**validated_data)
        punkt_peresadki.save()
        return Tranzit(**validated_data)


# Получить/отменить разрешение на полёт на данном летающем средстве
class RazrechenieNestedSerializer(serializers.ModelSerializer):
    id_plane = PlaneViewSerializer()
    id_ekipazha = EkipazhViewSerializer()

    class Meta:
        model = Razrechenie
        fields = "__all__"


class RazrechenieViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Razrechenie
        fields = "__all__"


class RazrechenieCreateSerializer(serializers.Serializer):
    id_plane = serializers.PrimaryKeyRelatedField(queryset=Plane.objects.all())
    id_ekipazha = serializers.PrimaryKeyRelatedField(queryset=Ekipazh.objects.all())

    razrechenie = serializers.BooleanField()

    def create(self, validated_data):
        razrechenie = Razrechenie(**validated_data)
        razrechenie.save()
        return Razrechenie(**validated_data)


# Рейс

class ReysViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reys
        fields = "__all__"


# Допуск на рейс
class DopuskNestedSerializer(serializers.ModelSerializer):
    number_reysa = ReysViewSerializer()
    id_ekipazha = EkipazhViewSerializer()

    class Meta:
        model = Dopusk
        fields = "__all__"


class DopuskViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dopusk
        fields = "__all__"


class DopuskCreateSerializer(serializers.Serializer):
    number_reysa = serializers.PrimaryKeyRelatedField(queryset=Reys.objects.all())
    id_ekipazha = serializers.PrimaryKeyRelatedField(queryset=Ekipazh.objects.all())

    nalichie_dopuska = serializers.BooleanField()

    def create(self, validated_data):
        dopusk = Dopusk(**validated_data)
        dopusk.save()
        return Dopusk(**validated_data)


# Полёт самолёта по рейсу
class PoletNestedSerializer(serializers.ModelSerializer):
    id_plane = PlaneViewSerializer()
    number_reysa = ReysViewSerializer()

    class Meta:
        model = Polet
        fields = "__all__"


class PoletViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polet
        fields = "__all__"