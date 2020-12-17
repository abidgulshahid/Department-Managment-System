from django.db import models
from teacher.models import Teacher
from student.models import Student
from users.models import Users
from department.models import batch_no


# Create your models here.

class HOD(models.Model):
	Department = models.OneToOneField('department.department', on_delete=models.CASCADE, default=None)
	hod_teachers_availables = models.ManyToManyField( "users.Users", related_name='Teacher_in_Current_Department')
	def __str__(self):
		return str(self.Department)


