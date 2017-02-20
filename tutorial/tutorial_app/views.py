from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class IndexView(TemplateView):
    template_name = 'tutorial_app/login.html'


class LoginSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'tutorial_app/home.html'


class Register(TemplateView):
    template_name = 'tutorial_app/register.html'


def register_user(request):
    data = request.POST
    User.objects.create_user(username=data['username'], email=data['email'],
    	first_name=data['first_name'], password=data['password'], last_name=data['last_name'])
    return login_user(request)


def login_user(request):
    data = request.POST
    username= data['username']
    password = data['password']
    user= authenticate(username=username, password=password)

    if user is not None:
    	login(request=request, user=user)
    else:
    	return HttpResponseRedirect(redirect_to='/')
    return HttpResponseRedirect(redirect_to='/success')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(redirect_to='/')    
