from django.urls import path
from . import viewsLogin

urlpatterns = [
    path('', viewsLogin.Login, name='Home'),
]
