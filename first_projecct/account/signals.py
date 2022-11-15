from .models import *
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print(instance)
        Profile.objects.create(user=instance,first_name=instance.first_name,last_name=instance.last_name)
    else:
        profile = Profile.objects.get(user=instance)
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.save()
