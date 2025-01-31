from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import BlogUser
from django.urls import reverse_lazy

# Create your views here.
class UserLoginView (LoginView):
    template_name = 'usersapp/login.html'


class UserCreateView(CreateView):
    model = BlogUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('usersapp:login')