from django.shortcuts import redirect
from functools import wraps
from authentication.models import Usuario


def login_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        if not request.session.get("username"):
            return redirect("authentication.login")
        return f(request, *args, **kwargs)
    return decorated_function
