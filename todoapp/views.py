from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .forms import LoginForm

# Create your views here.
class TodoList(LoginRequiredMixin, ListView):
    model = TodoModel
    template_name = 'list.html'


class TodoLogin(LoginView):
    form = LoginForm()
    template_name = 'login.html'
    # is_valid = form.is_valid()
    # if not is_valid:
    #     return render(request, 'login.html', {'form':form})

# class TodoLogin(AuthLoginView):
#     template_name = 'login.html'
    
class TodoLogout(LogoutView):
    template_name = 'logout.html'


class TodoCreate(LoginRequiredMixin, CreateView):
    model = TodoModel
    template_name = 'add.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('list')

class TodoDetail(LoginRequiredMixin, DetailView):
    model = TodoModel
    template_name = 'detail.html'

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = TodoModel
    template_name = 'edit.html'
    fields = ['title', 'content', 'is_done']
    success_url = reverse_lazy('list')

class TodoDelete(LoginRequiredMixin, DeleteView): 
    model = TodoModel
    template_name = 'delete.html'
    success_url = reverse_lazy('list')