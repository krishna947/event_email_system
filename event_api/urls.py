# event_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name='employee-list'),
    path('events/', views.EventList.as_view(), name='event-list'),
    path('event-templates/', views.EventTemplateList.as_view(), name='event-template-list'),
    path('email-logs/', views.EmailLogList.as_view(), name='email-log-list'),
]
