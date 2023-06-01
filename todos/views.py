from django.shortcuts import render, get_object_or_404
from todos.models import TodoList, TodoItem


# Create your views here.
def todo_list_list(request):
    list = TodoList.objects.all()
    context = {
        "todo_list_list": list,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    # list = TodoList.objects.get(id=id)
    list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_detail": list,
    }
    return render(request, "todos/detail.html", context)
