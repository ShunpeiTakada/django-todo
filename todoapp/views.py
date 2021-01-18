from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .forms import LoginForm

# Create your views here.
class TodoList(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoLogin(LoginView):
    template_name = 'login.html'
    form = LoginForm()
    # is_valid = form.is_valid()
    # if not is_valid:
    #     return render(request, 'login.html', {'form':form})
    
class TodoLogout(LogoutView):
    template_name = 'logout.html'


class TodoCreate(LoginRequiredMixin, CreateView):
    template_name = 'add.html'
    model = TodoModel
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('list')

class TodoDetail(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = TodoModel
    fields = ['title', 'content']
    success_url = reverse_lazy('list')