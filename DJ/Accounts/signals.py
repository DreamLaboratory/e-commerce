from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Profile, Account
user = get_user_model()


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save, sender=Account)
# def create_profile_save(sender, instance, created, **kwargs):
#     instance.profile.save()
