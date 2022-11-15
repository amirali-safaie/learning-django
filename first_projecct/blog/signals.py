from .models import *
from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver




@receiver(pre_delete, sender=Article)
def delet_Article(sender, instance, using, **kwargs):
    if using:
        print(instance.title)
