from django.urls import path
from . import viewsHospital

urlpatterns = [
    path('', viewsHospital.AddHospital, name='index'),
    path('ApplyBirthCertificate/',
         viewsHospital.ApplyBirthCertificate, name='ApplyBirthCertificate'),
    path('ApplyDeathCertificate/',
         viewsHospital.ApplyDeathCertificate, name='ApplyDeathCertificate'),
    path('PrintBirthCertificate/',
         viewsHospital.PrintBirthCertificate, name='PrintBirthCertificate'),
    path('PrintDeathCertificate/',
         viewsHospital.PrintDeathCertificate, name='PrintDeathCertificate'),
    path('RequestForUpdate/', viewsHospital.RequestForUpdate,
         name='RequestForUpdate'),
    path('ApplyBirthCertificateForm/', viewsHospital.ApplyBirthCertificateForm,
         name='ApplyBirthCertificateForm'),

    path('GetDistrict/<division_name>',
         viewsHospital.getDistrict, name="GetDistrict"),
    path('GetUpazila/<district_name>',
         viewsHospital.getUpazila, name="GetUpazila"),
    path('GetUnion/<upazila_name>', viewsHospital.getUnion, name="GetUnion"),
]
