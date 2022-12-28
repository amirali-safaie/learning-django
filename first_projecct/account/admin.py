from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[2][1]["fields"]=(     #hاضافه کردن فیلد های خودم به پنل ادمین
                                     "is_active",
                                     "is_staff",
                                     "is_superuser",
                                     "is_author",
                                     "special_user",
                                     "groups",
                                     "user_permissions",
                                     )

UserAdmin.list_display += ("is_author","special_or_not")

admin.site.register(User, UserAdmin)



# Register your models here.
