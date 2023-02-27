from django.db.models.signals import post_save
from .models import User, UserProfile
from django.dispatch import receiver
from ..common.send_email import send_email

@receiver(post_save, sender=User)
def createprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        send_email(email = instance.email)
        
