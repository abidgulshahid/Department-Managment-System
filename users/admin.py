from django.contrib import admin
from .models import Users
from django.contrib.auth.admin import UserAdmin
from department.models import *

# Register your models here.


class UsersAdmin(UserAdmin):
    model = Users
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                ('is_student',),
                ('is_teacher',),
                ('is_admin')
                
            
          



            )
        }
        ),
    )

admin.site.register(Users, UsersAdmin)


