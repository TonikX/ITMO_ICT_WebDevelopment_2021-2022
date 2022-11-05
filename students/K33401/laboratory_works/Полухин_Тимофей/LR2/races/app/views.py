from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic


@login_required(login_url='/login/')
def root_view(request):
    return render(request, 'index.html')
