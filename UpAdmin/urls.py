from django.urls import path
from . import viewsUpAdmin

urlpatterns = [
    path('', viewsUpAdmin.UpAdminHome, name="UpAdminHome"),
    path('UpAdminHome/', viewsUpAdmin.UpAdminHome, name="UpAdminHome"),
    path('VerifyNewChildInfo/<id>', viewsUpAdmin.VerifyNewChildInfo,
         name="VerifyNewChildInfo")
]
