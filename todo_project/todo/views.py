from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import ToDoModel
# Create your views here.


class ToDoList(ListView):
    template_name = 'list.html'
    model = ToDoModel


class ToDoDetail(DetailView):
    template_name = 'detail.html'
    model = ToDoModel


class ToDoCreate(CreateView):
    template_name = 'create.html'
    model = ToDoModel
    fields = ('title', 'memo', 'priority', 'due_date')
    success_url = reverse_lazy('list')


class ToDoDelete(DeleteView):
    template_name = 'delete.html'
    model = ToDoModel
    success_url = reverse_lazy('list')


class ToDoUpdate(UpdateView):
    template_name = 'update.html'
    model = ToDoModel
    fields = ('title', 'memo', 'priority', 'due_date')
    success_url = reverse_lazy('list')
