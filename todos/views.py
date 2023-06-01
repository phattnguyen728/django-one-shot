from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from .forms import TodoListForm, TodoItemForm


# Create your views here.
def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            todo_list = get_object_or_404(
                TodoList,
                name=form.cleaned_data["name"],
            )
            return redirect(todo_list_detail, todo_list.id)
    else:
        form = TodoListForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=list)
    context = {
        "form": form,
    }
    return render(request, "todos/edit.html", context)


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
