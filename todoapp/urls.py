from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('todoitem.urls')),
    path('', include('todofolder.urls')),
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
