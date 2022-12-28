from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser #کلاس یوزر خود جنگو که قرار ما توش ی سری فیلد اضافه کنیم

class User(AbstractUser):   #ارث بری از کلاس یوزر خود جنگو و ایجاد یوزر جدید برای استفاده توی پروژه
    is_author = models.BooleanField(default=False)
    special_user = models.DateTimeField(default=timezone.now)

    def special_or_not(self):
        if(timezone.now() < self.special_user):   #ایا یوزر الان یوزر طلایی هست یا ن
            return True
        else:
            return False
    special_or_not.boolean = True
    special_or_not.short_description = "special user"


# Create your models here.
