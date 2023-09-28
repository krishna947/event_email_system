from django.contrib import admin

# Register your models here.
from event_api.models import Employee, Event, EventTemplate, EmailLog

admin.site.register(Employee)
admin.site.register(Event)
admin.site.register(EventTemplate)
admin.site.register(EmailLog)