from django.db.models.signals import post_save
from .models import Account, UserProfile
from django.dispatch import receiver
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
import asyncio
from ..common.send_email import send_email_async


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        # TODO send email to user

        email = instance.email
        username = email.split("@")[0]  # get username from email
        instance.username = username
        instance.save()
        domain = '127.0.0.1:8000'
        domain = f"http://{domain}/activate/{urlsafe_base64_encode(force_bytes(instance))}/"
        subject = "Welcome to the site"
        message = f"Hi {instance.firstname}, welcome to the site"
        body = render_to_string(
            "accounts/verification.html",
            {
                "subject": subject,
                "body": message,
                "domain": domain,
            },
        )
        html_body = strip_tags(body)
        asyncio.run(send_email_async(subject, html_body, [email]))

