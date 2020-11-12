from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.urls import reverse

import datetime
# Create your models here.

SEMSESTER_CHOICES = (
    (1, "SPRING"),
    (2, "FALL")
)
STUDENT_YEAR_CHOICE = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8")
)


class Users(AbstractUser):
    username = models.CharField(max_length=200, unique=True, null=True)
    email =models.EmailField(max_length=200, unique=True, null=True)
    cnic =models.CharField(max_length=200,null=True)
    city =models.CharField(max_length=200,null=True)
    address =models.CharField(max_length=200,null=True )
    is_teacher = models.BooleanField(default=False, help_text='True if the User is a Teacher.')
    is_student = models.BooleanField(default=False, help_text='True if the User is a Student.')
    GENDERS = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('U', 'UNDEFINED'),
        ('O', 'OTHER')
    ]
    gender = models.CharField(
        "Gender", name="gender", max_length=50, choices=GENDERS)


    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # @classmethod
    # def create(cls, username, password, is_teacher=False, is_maintainer=False, is_student=False, is_employee=False, is_faculty=False, employee=None, *args, **kwargs):
    #
    #     user = cls(username=username, is_teacher=is_teacher, is_maintainer=is_maintainer, is_student=is_student,
    #                is_employee=is_employee, is_faculty=is_faculty, employee=employee, *args, **kwargs)
    #     user.set_password('hassan')
    #     user.save()
    #     if user.is_staff:
    #         user.groups.add(Group.objects.get(name='maintainer_group'))
    #         print('Added ' + str(user) + ' in ' + 'maintainer_group')
    #     if user.is_student:
    #         user.groups.add(Group.objects.get(name='student_group'))
    #         print('Added ' + str(user) + ' in ' + 'student_group')
    #     if user.is_teacher:
    #         user.groups.add(Group.objects.get(name='teacher_group'))
    #         print('Added ' + str(user) + ' in ' + 'teacher_group')
    #
    #
    #     return user
