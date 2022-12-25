from django.shortcuts import render
  
# relative import of forms
from .models import CarOwner
from .forms import OwnerForm # импортируем только-что созданную форму
    
def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = OwnerForm(request.POST or None) # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid(): # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "owner_create_form.html", context)