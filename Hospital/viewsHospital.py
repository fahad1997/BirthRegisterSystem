from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Count
from BirthRegisterSystem.models import Area
from .models import NewChildInfo
import json
import datetime


def AddHospital(request):
    return render(request, 'HospitalIndex.html')


def ApplyBirthCertificate(request):
    Division = Area.objects.values(
        'Division_name').distinct().order_by('Division_name')
    return render(request, 'ApplyBirthCertificate.html', {'Division': Division})


def ApplyDeathCertificate(request):
    return render(request, 'ApplyDeathCertificate.html')


def PrintBirthCertificate(request):
    childInfo = NewChildInfo.objects.filter(Validation=1)
    return render(request, 'PrintBirthCertificate.html', {'childInfo': childInfo})


def PrintDeathCertificate(request):
    return render(request, 'PrintDeathCertificate.html')


def RequestForUpdate(request):
    return render(request, 'RequestForUpdate.html')


def ApplyBirthCertificateForm(request):
    name = request.POST["name"]
    blood_group = request.POST["blood_group"]
    birth_date = request.POST["birth_date"]
    father_name = request.POST["father_name"]
    father_nid = request.POST["father_nid"]
    mother_name = request.POST["mother_name"]
    religion = request.POST["religion"]
    division = request.POST["DropDownDivision"]
    district = request.POST["DropDownDistrict"]
    upazila = request.POST["DropDownUpazila"]
    union = request.POST["DropDownUnion"]
    new_child_info = NewChildInfo(Name=name, Blood_group=blood_group, Birth_Date=birth_date,
                                  Father_name=father_name, Father_NID=father_nid,
                                  Mother_name=mother_name, Religion=religion, Division_name=division,
                                  District_name=district, Upazila_name=upazila, Union_name=union)
    new_child_info.save()
    return render(request, 'ApplyBirthCertificate.html')


def getDistrict(request, division_name):
    Districts = Area.objects.filter(Division_name=division_name).values(
        'District_name').distinct().order_by('District_name')
    return JsonResponse({"Districts": list(Districts)})


def getUpazila(request, district_name):
    Upazilas = Area.objects.filter(District_name=district_name).values(
        'Upazila_name').distinct().order_by('Upazila_name')
    return JsonResponse({"Upazilas": list(Upazilas)})


def getUnion(request, upazila_name):
    Unions = Area.objects.filter(Upazila_name=upazila_name).values(
        'Union_name').distinct().order_by('Union_name')
    return JsonResponse({"Unions": list(Unions)})
