from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from authentication.forms import CreateUserForm


# Create your views here.
sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'oldpassword', 'password', 'password1', 'password2'))

class LoginUserView(LoginView):
    template_name = "authentication/form.html"


class UserChangePasswordView(PasswordChangeView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy("") #aici e de pus unde te trimite dupa ce ai adaugat parola corecta


class CreateUserView(CreateView):
    template_name = "authentication/form.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("")  # aici dupa ce este format user-ul (felicitarii,cont facut cu succes,etc).

class LogOutUserView(LogoutView):
    success_url = reverse_lazy("")  # aici dupa ce iesi din cont, template de facut.
