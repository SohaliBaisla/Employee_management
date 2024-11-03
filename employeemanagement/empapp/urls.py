from django.urls import path, include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register("Employee_details", EmployeeViewSet)
router.register("Company_details", CompanyViewSet)
router.register("Project_details", ProjectViewSet)

urlpatterns=[
    path('emp/',include(router.urls)),
]