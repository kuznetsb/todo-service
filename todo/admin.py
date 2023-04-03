from django.contrib import admin

from todo.models import Tag, Task


admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "content", "datetime", "deadline_datetime", "is_done"
    ]
    list_filter = ["is_done", "tags", "deadline_datetime"]
    search_fields = ["content"]
