from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView 

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoLogin(LoginView):
    template_name = 'login.html'

class TodoLogout(LogoutView):
    template_name = 'logout.html'

class TodoCreate(CreateView):
    template_name = 'add.html'
    model = TodoModel
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('list')

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoUpdate(UpdateView):
    template_name = 'edit.html'
    model = TodoModel
    fields = ['title', 'content']
    success_url = reverse_lazy('list')