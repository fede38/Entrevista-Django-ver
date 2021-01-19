from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='todofolder.index'),
    path('/create', views.create, name='todofolder.create'),
    path('/<int:id_>/delete', views.delete, name='todofolder.delete'),
]
