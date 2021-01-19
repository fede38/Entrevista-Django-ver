from django.shortcuts import render, redirect
from .models import ToDoFolder


def index(request):
    folders = ToDoFolder.objects.all()
    return render(request, 'todofolder/index.html', {'folders': folders})


def create(request):
    folder = ToDoFolder(description=request.POST["folder_name"])
    folder.save()
    return redirect('todofolder.index')


def delete(request, id_):
    p = ToDoFolder.objects.get(id=id_)
    p.delete()
    return redirect('todofolder.index')
