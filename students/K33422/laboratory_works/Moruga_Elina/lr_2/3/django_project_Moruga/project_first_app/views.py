from django.shortcuts import render
from django.http import Http404 
from .models import CarOwner

def detail(request, owner_id):
    try: #метод try-except - обработчик исключений
        p = CarOwner.objects.get(pk=owner_id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'detail.html', {'owner': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"



