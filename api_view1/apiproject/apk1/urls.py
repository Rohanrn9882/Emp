from django.urls import path
from apk1.views import EmployeeInfo, EmployeeDetails

urlpatterns = [
    path('emp', EmployeeInfo.as_view()),
    path('emp/<int:id>', EmployeeDetails.as_view()),
]