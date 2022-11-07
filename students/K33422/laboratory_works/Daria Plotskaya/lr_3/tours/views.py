from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Tour, Reservation, Review
from .serializers import TourSerializer, ReservationReadSerializer, ReservationWriteSerializer, TourAndReviewsSerializer, ReviewSerializer


# Список доступных туров / Информация о туре + отзывы
class TourViewSet(ReadOnlyModelViewSet):
    queryset = Tour.objects.order_by("destination")  # Туры сортируются по стране

    # Показывает только те туры где есть место
    def get_queryset(self):
        queryset = self.queryset
        ids = [tour.id for tour in queryset if tour.empty_count > 0]
        return queryset.filter(pk__in=ids)

    # Выдает разный сериализатор в зависимости от того, требуется ли список туров или конкретный тур
    def get_serializer_class(self):
        if self.action == 'list':
            return TourSerializer
        else:
            return TourAndReviewsSerializer


# Список резервирований пользователя
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.none()  # Задаем queryset чтобы django не выдавал ошибку

    # Выбирает только резервирования текущего пользователя
    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user.id)

    # Выдает разный сериализатор для чтения и для записи
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return ReservationWriteSerializer
        else:
            return ReservationReadSerializer


# Отзывы
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.none()  # Задаем queryset чтобы django не выдавал ошибку
    serializer_class = ReviewSerializer

    # Выбирает только отзывы текущего пользователя
    def get_queryset(self):
        return Review.objects.filter(reservation__user=self.request.user.id)
