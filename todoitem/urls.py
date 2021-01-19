from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_>/', views.index, name='todoitem.index'),
    path('<int:id_>/create', views.create, name='todoitem.create'),
    path('<int:id_>/edit/<int:id_2>', views.edit, name='todoitem.edit'),
    path('<int:id_>/delete/<int:id_2>', views.delete, name='todoitem.delete'),
    path('<int:id_>/check/<int:id_2>', views.check, name='todoitem.check'),
]
