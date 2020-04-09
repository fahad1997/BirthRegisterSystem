from django.shortcuts import render
from django.http import HttpRequest


def Login(request):
    return render(request, 'Home.html')
