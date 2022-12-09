from django.http import Http404 #импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render #импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from .models import CarOwner #импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)
from .forms import ExampleForm
def detail(request, carowner_id):
    try: #метод try-except - обработчик исключений
        c = CarOwner.objects.get(pk=carowner_id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except CarOwner.DoesNotExist:
        raise Http404("Car does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'detail.html', {'CarOwner': c}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"


def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь 
    context["dataset"] = CarOwner.objects.all()
          
    return render(request, "list_view.html", context)

def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = ExampleForm(request.POST or None) # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid(): # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)
