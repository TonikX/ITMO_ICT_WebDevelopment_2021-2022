from django.shortcuts import render
from .models import CarOwner
  
  
def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь 
    context["dataset"] = CarOwner.objects.all()
          
    return render(request, "list_views_func.html", context)