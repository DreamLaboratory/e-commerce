from .models import MyUser, MyUserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        MyUserProfile.objects.create(user=instance)
