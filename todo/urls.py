from django.urls import path

from todo.views import TaskList


urlpatterns = [
    path("", TaskList.as_view(), name="index")
]

app_name = "todo"
