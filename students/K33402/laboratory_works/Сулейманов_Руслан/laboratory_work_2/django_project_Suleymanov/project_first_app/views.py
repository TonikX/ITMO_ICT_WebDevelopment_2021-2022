from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Owner

# Create your views here.
def owners(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'owner.html', {'owner': p})