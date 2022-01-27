from .models import Reviews, Users, Tours, Bookings
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

class ReviewCreateView(CreateView):
  model = Reviews
  fields = ['content', 'rate']
  success_url = '/reviews_list/'
  template_name = 'reviews_create_form.html'

  def post(self, request, *args, **kwargs):
    qudi = request.POST
    booking = self.request.GET.get('booking')[:-1]
 
    if booking:
      user = Users.objects.all().filter(username=self.request.user)
      bk = Bookings.objects.all().filter(id=booking)
      tour = bk[0].id_tour
 
      Reviews.objects.create(id_user=user[0], 
                              id_tour=tour,
                              content=qudi['content'],
                              rate=qudi['rate'],
                              date_start=tour.date_start,
                              date_end=tour.date_end)
 
    return HttpResponseRedirect(self.success_url)