from django.shortcuts import render
from todos.models import TodoList


# Create your views here.
def todo_list_list(request):
    lists = TodoList.objects.all()
    context = {
        "todo_list_list": lists,
    }
    return render(request, "todos/list.html", context)
