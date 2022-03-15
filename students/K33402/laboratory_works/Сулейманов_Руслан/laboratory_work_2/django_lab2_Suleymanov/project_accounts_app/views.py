from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request, "account/account.html", {"user": request.user})
