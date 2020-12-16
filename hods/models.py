from django.db import models
from teacher.models import Teacher
from student.models import Student
from users.models import Users
from department.models import batch_no


# Create your models here.

class HOD(models.Model):
	HOD_Teachers = models.OneToOneField('users.Users', on_delete=models.CASCADE, default=None)
	Department = models.OneToOneField('department.department', on_delete=models.CASCADE, default=None)

	def __str__(self):
		return str(self.Department)

