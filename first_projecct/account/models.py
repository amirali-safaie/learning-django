from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    special_user= models.DateTimeField(default=timezone.now)

    def special_or_not(self):
        if(timezone.now<self.special_user):
            return True
        else:
            return False



# Create your models here.
