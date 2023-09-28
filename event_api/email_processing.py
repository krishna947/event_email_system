# event_api/email_processing.py

import logging

from django.core.mail import send_mail
from django.utils import timezone

from celery import shared_task
from event_api.models import EmailLog, Employee, Event, EventTemplate


@shared_task()
def send_emails_for_today_events():
    logging.info("Sending event task called.")
    today = timezone.now().date()
    events = Event.objects.filter(event_date=today)

    if not events:
        logging.info("No events scheduled for today.")
        return

    for event in events:
        try:
            employee = event.employee
            event_type = event.event_type
            event_date = event.event_date

            template = EventTemplate.objects.get(event_type=event_type)
            email_template = template.template_content

            # Populate email template with event-specific content
            email_content = email_template.format(
                employee_name=employee.name,
                event_type=event_type,
                event_date=event_date,
            )

            # Send the email
            send_mail(
                f"Event Notification: {event_type}",
                email_content,
                'krishna.gupta@doselect.com',
                [employee.email],
                fail_silently=False,
            )

            # Log successful email
            EmailLog.objects.create(
                employee=employee,
                event_type=event_type,
                event_date=event_date,
                status='Sent',
            )

            logging.info(f"Email sent to {employee.email} for {event_type} on {event_date}")

        except Exception as e:
            # Log the error and continue processing other events
            EmailLog.objects.create(
                employee=employee,
                event_type=event_type,
                event_date=event_date,
                status='Failed',
                error_message=str(e),
            )

            logging.error(f"Error sending email to {employee.email} for {event_type}: {e}")

    logging.info("Sending event task completed.")