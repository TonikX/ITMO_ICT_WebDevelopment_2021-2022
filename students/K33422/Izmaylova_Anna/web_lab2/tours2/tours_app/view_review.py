from django.views.generic.list import ListView
from .models import Reviews, Tours
from .models import Reviews, Users, Tours, Bookings
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

# представление для отображения списка отзывов
class ReviewList(ListView):
  model = Reviews
  template_name = 'list_reviews.html'
  queryset = model.objects.all()

  def get_queryset(self):
    tour = self.request.GET.get('tour')

    if tour:
      # отфильтровать тур, к которому хотим показать отзывы
      tour = Tours.objects.all().filter(id=tour)

      # отфильтровать отзывы по этому туру
      queryset = self.queryset.filter(id_tour=tour)
      return queryset
    else:
      return self.queryset

# представление для создания отзывов
class ReviewCreateView(CreateView):
  model = Reviews
  fields = ['content', 'rate'] # указываем, какие поля отзывов можно заполнять при создании
  success_url = '/reviews_list/' # на какой адрес перейти после успешного создания отзыва
  template_name = 'reviews_create_form.html'

  # метод для записи отзыва в базу данных
  def post(self, request, *args, **kwargs):
    qudi = request.POST
    booking = self.request.GET.get('booking')[:-1]
 
    if booking:
      # ищем пользователя, который оставил отзыв
      user = Users.objects.all().filter(username=self.request.user)

      # ищем бронирование, о котором оставлен отзыв
      bk = Bookings.objects.all().filter(id=booking)
      tour = bk[0].id_tour
 
      # создаем новую запись в БД
      Reviews.objects.create(id_user=user[0], 
                              id_tour=tour,
                              content=qudi['content'],
                              rate=qudi['rate'],
                              date_start=tour.date_start,
                              date_end=tour.date_end)

    # redirect - перенаправление по адресу из self.success_url
    return HttpResponseRedirect(self.success_url)