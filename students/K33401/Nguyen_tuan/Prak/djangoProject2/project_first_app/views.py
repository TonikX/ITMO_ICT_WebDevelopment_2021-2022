from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import OwerUser
def detail(request, id):
    p = {}
    try:
        p['dataset'] = OwerUser.objects.get(pk = id)
    except OwerUser.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'OwerUser.html', p)
def detail1(request):
    q = {}
    try:
        q['dataset'] = OwerUser.objects.all()
    except OwerUserr.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'OwerUser1.html', q)
