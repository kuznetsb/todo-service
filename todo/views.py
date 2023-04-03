from django.shortcuts import render
from django.views import generic

from todo.models import Task


class TaskList(generic.ListView):
    model = Task
    ordering = ["is_done", "-datetime"]
    queryset = Task.objects.prefetch_related("tags")
