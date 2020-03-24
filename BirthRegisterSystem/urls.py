from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddArea, name='index'),
    path('AddAreaForm/', views.AddArea, name="AddArea"),
    path('AddArea/', views.add_area_form, name="add_area_form"),

    path('AddUpazilaAdmin/', views.add_upazila_admin, name="add_upazila_admin"),
    path('AddUpazilaAdminForm/', views.add_upazila_admin_form,
         name="add_upazila_admin_form"),

    path('AddHospitalForm/', views.add_hospital_form, name="add_hospital_form"),
    path('AddHospital/', views.add_hospital, name="add_hospital"),

    path('GetDistrict/<division_name>', views.getDistrict, name="GetDistrict"),
    path('GetUpazila/<district_name>', views.getUpazila, name="GetUpazila"),
    path('GetUnion/<upazila_name>', views.getUnion, name="GetUnion"),
    path('AllInformation/', views.allinformation, name="allinformation"),
    path('districtInformation/', views.districtInformation, name="districtInformation"),
]
