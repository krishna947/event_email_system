# event_api/models.py

from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


EVENT_TYPE_CHOICES = (
    ('birthday', 'Birthday'),
    ('anniversary', 'Work Anniversary'),
    ('other', 'Other'),
)

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100, choices=EVENT_TYPE_CHOICES)
    event_date = models.DateField()

class EventTemplate(models.Model):
    event_type = models.CharField(max_length=100, choices=EVENT_TYPE_CHOICES)
    template_content = models.TextField()

class EmailLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    sent_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20)
    error_message = models.TextField(blank=True, null=True)
