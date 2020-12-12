from django.db import models
from users.models import Users
from department.models import batch_no
# Create your models here.

class Student(models.Model):
    # @classmethod
    # def create(cls, first_name, last_name, email, password, *args, **kwargs):
    #     print(first_name + last_name + email + password)
    #     user_created = Users(first_name=first_name, last_name=last_name,
    #                         password=password, email=email, is_student=True)
    #     user_created.save()
    #     # last_student = Student.objects.all().order_by('arn').last()
    #     #
    #     # if not last_student:
    #     #     print("last student is empty")
    #     #     last_arn_number = ((17 % 100)*1000000)+1
    #     # else:
    #     #     last_arn_number = last_student.arn + 1
    #
    #     student_created = cls(use=user_created)
    #
    #     student_created.groups.add(Group.objects.get(name='student_group'))
    #     print("Returning created student")
    #     print(student_created)
    #
    #     return student_created
    students = models.OneToOneField('users.Users', on_delete=models.CASCADE, default=None)
    std = models.ForeignKey('department.batch_no', on_delete=models.SET_NULL,default=None,blank=True, null=True)
    uid = models.AutoField(primary_key=True)
    def __str__(self):
        return self.students.username
