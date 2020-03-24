from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Count
from .models import Area
from .models import UpAdmin
from .models import Hospital
from .models import AddDistrict
import json


def AddArea(request):
    return render(request, 'AddArea.html')

def districtInformation(request):
    return render(request,'dropdown.html')

def allinformation(request):
    district = request.POST["adddistrict"]
    district_info = AddDistrict(AddDistrict=district)
    district_info.save()
    District = AddDistrict.objects.values(
        'AddDistrict').distinct().order_by('AddDistrict')
    return render(request, 'dropdown.html', {'District': District})


def add_area_form(request):
    division = request.POST["division_input_field"]
    district = request.POST["district_input_field"]
    upazila = request.POST["upazila_input_field"]
    union = request.POST["union_input_field"]

    area_info = Area(Division_name=division, District_name=district,
                     Upazila_name=upazila, Union_name=union)
    area_info.save()
    return render(request, 'AddArea.html')


def add_upazila_admin(request):
    division = request.POST["DropDownDivision"]
    district = request.POST["DropDownDistrict"]
    upazila = request.POST["DropDownUpazila"]
    u_username = request.POST["u_username"]
    u_password = request.POST["u_password"]
    upazila_admin_info = UpAdmin(Division_name=division, District_name=district,
                                 Upazila_name=upazila, U_username=u_username, U_password=u_password)
    upazila_admin_info.save()
    return render(request, 'AddUpazilaAdmin.html')


def add_hospital(request):
    hospital_name = request.POST["hospitalname"]
    division = request.POST["DropDownDivision"]
    district = request.POST["DropDownDistrict"]
    upazila = request.POST["DropDownUpazila"]
    union = request.POST["DropDownUnion"]
    h_username = request.POST["h_username"]
    h_password = request.POST["h_password"]
    hospital_info = Hospital(H_name=hospital_name, Division_name=division, District_name=district,
                             Upazila_name=upazila, H_username=h_username, H_password=h_password)
    hospital_info.save()
    return render(request, 'AddHospital.html')


def add_hospital_form(request):
    Division = Area.objects.values(
        'Division_name').distinct().order_by('Division_name')
    return render(request, 'AddHospital.html', {'Division': Division})


def add_upazila_admin_form(request):
    Division = Area.objects.values(
        'Division_name').distinct().order_by('Division_name')
    return render(request, 'AddUpazilaAdmin.html', {'Division': Division})


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
