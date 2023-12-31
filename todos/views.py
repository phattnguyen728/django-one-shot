from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from .forms import TodoListForm, TodoItemForm


# Create your views here.
def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            item = form.save()
            todo_list = get_object_or_404(
                TodoList,
                name=form.cleaned_data["name"],
            )
            return redirect(todo_list_detail, id=item.id)
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


def todo_list_delete(request, id):
    # list = TodoList.objects.get(id=id)
    list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        list.delete()
        return redirect("todo_list_list")
    else:
        return render(request, "todos/delete.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            # list = get_object_or_404(
            #     TodoList,
            #     name=form.cleaned_data["list"],
            # )
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()
    context = {
        "form": form,
    }
    return render(request, "todos/items/create.html", context)


def todo_item_update(request, id):
    item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm(instance=item)
    context = {
        "form": form,
    }
    return render(request, "todos/items/edit.html", context)


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
