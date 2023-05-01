from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    ordering = ["is_done", "-datetime"]
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


def complete_undo_task(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect(reverse_lazy("todo:task-list"))
