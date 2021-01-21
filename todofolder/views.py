from django.shortcuts import render, redirect
from .models import ToDoFolder
from todoapp.helpers import login_required
from authentication.models import Usuario


@login_required
def index(request):
    user = Usuario.objects.get(usuario=request.session["username"])
    folders = ToDoFolder.objects.filter(user=user)
    return render(request, 'todofolder/index.html', {'folders': folders})


@login_required
def create(request):
    user = Usuario.objects.get(usuario=request.session["username"])
    folder = ToDoFolder(description=request.POST["folder_name"], user=user)
    folder.save()
    return redirect('todofolder.index')


@login_required
def delete(request, id_):
    p = ToDoFolder.objects.get(id=id_)
    p.delete()
    return redirect('todofolder.index')
