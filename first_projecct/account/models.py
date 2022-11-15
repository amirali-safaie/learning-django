from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=200,blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


    def __str__(self):
        return str(self.user)



# Create your models here.
