from celery import shared_task
from django.core.management import call_command


# @shared_task(bind=True)
# def run_campaigns_daily(self):
#     call_command('create_campaigns')


# campaign_manager/tasks.py
import requests
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import *
from datetime import date

@shared_task
def send_daily_campaigns():
    # Retrieve today's campaigns
    today_campaigns = Campaign.objects.filter(published_date=date.today())



    for campaign in today_campaigns:
        # Render email content from a template
        email_html = render_to_string('custom_email_template.html', {'campaign': campaign})

        # Send email using SMTP (replace with your Mailgun sandbox details)
        send_mail(
            subject=campaign.subject,
            message=campaign.preview_text,
            from_email='sainrk98@gmail.com',  # Replace with your Mailgun sandbox sender address
            recipient_list=[subscriber.email for subscriber in Subscriber.objects.filter(is_active=True)],
            html_message=email_html,
        )
