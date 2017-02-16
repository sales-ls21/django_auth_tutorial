from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse

# Create your views here.

class IndexView(TemplateView):
    template_name = 'tutorial_app/login.html'


class LoginSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'tutorial_app/home.html'


class Register(TemplateView):
    template_name = 'tutorial_app/register.html'


def register_user(request):
    pass


def login_user(request):
    pass


def logout_user(request):
    pass
