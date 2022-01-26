from django.contrib.auth import authenticate, login
from django.views.generic import FormView, View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView as BaseLoginView
from django.forms import ValidationError
from django.core.mail import send_mail

from .forms import UserCreationForm
from .models import User


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        code = str(user.code)

        link = self.request.build_absolute_uri(reverse('accounts:confirm', kwargs={'code': code}))

        send_mail('Elevennote activation link', f'Here is your Elevennote account activation link',
                  'elevennote@komarov.ml', [user.email], fail_silently=False,
                  html_message=f'Here is your Elevennote account activation link: <a href={link}>click here</a>')

        return render(self.request, 'registration/confirm.html',
                      {'text': 'Your account is now created. Please, follow link in your mail box for confirmation.'})


class LoginView(BaseLoginView):
    def form_valid(self, form):
        """Security check complete. Log the user in if activated."""
        user = form.get_user()
        if user.is_confirmed or user.is_superuser:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return render(self.request, 'registration/confirm.html',
                          {'text': 'Your account is not confirmed. Please, follow link in your mail box.'})


def confirm(request, code):
    try:
        user = User.objects.get(code=code)
        user.is_confirmed = True
        user.save()

        login(request, user)

        return render(request, 'registration/confirm.html',
                      {'text': 'Your account is now confirmed.'})
    except (User.DoesNotExist, ValidationError):
        return render(request, 'registration/confirm.html', {'text': 'Invalid link.'})
