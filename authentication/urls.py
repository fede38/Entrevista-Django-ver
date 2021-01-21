from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='authentication.login'),
    path('logout/', views.logout, name='authentication.logout'),
    path('register/', views.register, name='authentication.register'),
]