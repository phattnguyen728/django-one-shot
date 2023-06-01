from django.forms import ModelForm
from django import forms
from .models import TodoList, TodoItem


class TodoListForm(ModelForm):
    # name = forms.CharField(max_length=100)
    class Meta:
        model = TodoList
        fields = [
            "name",
        ]


class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "task",
            "due_date",
            "is_completed",
        ]
