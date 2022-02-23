from rest_framework import serializers
from .models import Tour, Reservation, Review


# Сериализатор для туров (только для чтения)
class TourSerializer(serializers.ModelSerializer):
    empty_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tour
        fields = ("id", "destination", "date_from", "date_to", "hotel", "price", "empty_count")
        read_only_fields = ("id", "destination", "date_from", "date_to", "hotel", "price", "empty_count")


# Сериализатор для резервирований (для чтения)
class ReservationReadSerializer(serializers.ModelSerializer):
    tour = TourSerializer()
    total_price = serializers.IntegerField()
    has_review = serializers.BooleanField()

    class Meta:
        model = Reservation
        fields = ("id", "tour", "count", "approved", "total_price", "has_review")
        read_only_fields = ("id", "tour", "count", "approved", "total_price", "has_review")


# Сериализатор для резервирований (для записи)
class ReservationWriteSerializer(serializers.ModelSerializer):
    tour = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Tour.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reservation
        fields = ("tour", "user", "count", "total_price")
        read_only_fields = ("total_price",)

    def validate(self, attrs):
        count = attrs["count"]
        tour = attrs["tour"]
        if self.instance:
            # Если объект существует, исплючаем его из счета
            if count > tour.adjusted_empty_count(exclude_id=self.instance.pk):
                raise serializers.ValidationError("Недостаточно мест")
        else:
            if count > tour.empty_count:
                raise serializers.ValidationError("Недостаточно мест")
        return attrs


# Сериализатор для отзывов
class ReviewSerializer(serializers.ModelSerializer):
    # Явно указываем что ID резервирования не должен отображаться при чтении (для анонимности отзывов)
    reservation = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Reservation.objects.all())
    name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ("id", "reservation", "text", "stars", "name")
        read_only_fields = ("id", "name",)

    def get_name(self, obj):
        return obj.reservation.user.anonimous_name

    # Разрешаем оставлять отзыв только на подтвержденое резервирование, только на свое резервирование и только 1 раз
    def validate(self, attrs):
        reservation = attrs["reservation"]
        if not reservation.approved:
            raise serializers.ValidationError("Нельзя оставлять отзыв без подтвержденного резервирования")
        if reservation.has_review:
            raise serializers.ValidationError("Вы уже оставили отзыв")
        if reservation.user != self.context["request"].user:
            raise serializers.ValidationError("Нельзя оставлять отзывы на чужие резервирования")
        return attrs


# Сериализатор для туров с отзывами (только для чтения)
class TourAndReviewsSerializer(TourSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta(TourSerializer.Meta):
        fields = TourSerializer.Meta.fields + ("reviews",)
        read_only_fields = TourSerializer.Meta.read_only_fields + ("reviews",)

    # Функция для получения списка сериализованных отзывов
    def get_reviews(self, obj):
        review_ids = []
        for reservation in obj.reservations.all():
            if reservation.has_review:
                review_ids.append(reservation.review.pk)
        queryset = Review.objects.filter(pk__in=review_ids)
        return ReviewSerializer(queryset, many=True).data
