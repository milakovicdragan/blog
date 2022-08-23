# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    #we use reverse_lazy to redirect the user to the log in page upon successful registration.
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
