from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# View for sign up
class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = "users/sign_up.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
