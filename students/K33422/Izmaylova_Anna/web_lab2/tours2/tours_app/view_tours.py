from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tours
import datetime
  
# представление для отображения списка туров
class TourList(ListView):
    model = Tours 
    template_name = 'list_tours.html'
    queryset = model.objects.all() # получить все записи в из таблицы модели

    # функция, которая фильтрует записи из queryset
    def get_queryset(self):
        # из запроса 127.0.0.1:8000/tours_list/?country=рф в переменную country
        # запишется рф
        country = self.request.GET.get('country')
        
        # пользователь мог не писать параметр country
        # условие срабатывает, если его написали, иначе переходит к строке 29
        if country:
            try:
                # отфильтровать туры по стране
                queryset = self.queryset.filter(country=country)
                
                # отфильтровать туры по дате (взять продшие, lte = меньше)
                queryset = queryset.filter(date_end__lte=datetime.date.today())
            except ValueError:
                # если произошла ошибка, то вернуть ничего
                queryset = self.model.objects.none()

            # вернуть отфильтрованные значения
            return queryset
        else:
            # вернуть будущие туры (gte = больше)
            return self.queryset.filter(date_end__gte=datetime.date.today())

# представление для отображения одного тура
class TourRetrieveView(DetailView):
    model = Tours
    template_name = 'tour_detail.html'