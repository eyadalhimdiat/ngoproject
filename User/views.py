from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'registration/signup.html')

def edit_user(request, id):
    return render(request, 'edit_user.html')


def delete_user(request,id):
    return render(request, 'delet_user.html')

