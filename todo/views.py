from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
    ordering = ["is_done", "-datetime"]
    queryset = Task.objects.prefetch_related("tags")
