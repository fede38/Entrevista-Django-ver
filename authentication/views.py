from django.shortcuts import render, redirect
from todoapp.helpers import login_required
from .models import Usuario
from django.contrib import messages


def autenticar(user, password):
    return user.password == password


def login(request):
    if not request.session.get("username"):
        if request.method == 'POST':
            if request.POST.get("username"):
                try:
                    user = Usuario.objects.get(usuario=request.POST.get("username"))
                except Usuario.DoesNotExist:
                    return render(request, 'authentication/login.html', {})
                if autenticar(user, request.POST.get("password")):
                    request.session["username"] = user.usuario
                    return redirect('todofolder.index')
                else:
                    return render(request, 'authentication/login.html', {})
        return render(request, 'authentication/login.html', {})
    return redirect('todofolder.index')


def register(request):
    if request.method == "POST":
        user = Usuario.objects.filter(usuario=request.POST.get("username"))
        if not user:
            user = Usuario(
                usuario=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            user.save()
            return redirect('authentication.login')
    return render(request, 'authentication/register.html')


@login_required
def logout(request):
    del request.session["username"]
    return redirect('authentication.login')
