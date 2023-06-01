from django.contrib import admin
from .models import TodoList, TodoItem


# Register your models here.
@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "created_on",
    )


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "due_date",
        "todo_list_list",
        "id",
        "is_completed",
    )
