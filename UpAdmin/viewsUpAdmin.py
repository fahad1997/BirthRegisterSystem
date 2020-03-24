from django.shortcuts import render, redirect
from django.http import HttpResponse
from Hospital.models import NewChildInfo
from django.db import IntegrityError


def UpAdminHome(request):
    childInfo = NewChildInfo.objects.all().filter(Validation=False)
    return render(request, 'UPAdminHomePage.html', {'childInfo': childInfo})


def VerifyNewChildInfo(request, id):
    update = NewChildInfo.objects.filter(id=id).update(Validation=True)
    return render(request, 'UPAdminHomePage.html')
