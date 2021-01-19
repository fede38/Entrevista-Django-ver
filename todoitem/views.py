from django.shortcuts import render, redirect
from todofolder.models import ToDoFolder
from .models import ToDoItem


def index(request, id_):
    folder = ToDoFolder.objects.get(id=id_)
    items = folder.todoitem_set.all()
    return render(request, 'todoitem/index.html', {'items': items, 'folder': folder})


def create(request, id_):
    folder = ToDoFolder.objects.get(id=id_)
    item = ToDoItem(description=request.POST["item_name"])
    item.folder = folder
    item.save()
    return redirect('todoitem.index', id_=id_)


def check(request, id_, id_2):
    item = ToDoItem.objects.get(id=id_2)
    try:
        checkbox = request.POST["item_check"]
        item.checked = True
    except:
        item.checked = False
    finally:
        item.save()
    return redirect('todoitem.index', id_=id_)


def edit(request, id_, id_2):
    folder = ToDoFolder.objects.get(id=id_)
    item = ToDoItem.objects.get(id=id_2)
    if request.method == "POST":
        item.description = request.POST["item_name"]
        item.save()
        return redirect('todoitem.index', id_=id_)
    return render(request, "todoitem/edit.html", {'folder': folder, 'item': item})


def delete(request, id_, id_2):
    p = ToDoItem.objects.get(id=id_2)
    p.delete()
    return redirect('todoitem.index', id_=id_)