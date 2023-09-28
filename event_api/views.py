# event_api/views.py
import logging
from rest_framework import generics
from event_api.models import Employee, Event, EventTemplate, EmailLog
from event_api.serializers import EmployeeSerializer, EventSerializer, EventTemplateSerializer, EmailLogSerializer

class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventTemplateList(generics.ListAPIView):
    queryset = EventTemplate.objects.all()
    serializer_class = EventTemplateSerializer

class EmailLogList(generics.ListAPIView):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer
