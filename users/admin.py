from django.contrib import admin
from .models import Users
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UsersAdmin(UserAdmin):
    model = Users

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                ('is_student',),
                ('is_teacher',),



            )
        }
        ),
    )

admin.site.register(Users, UsersAdmin)
