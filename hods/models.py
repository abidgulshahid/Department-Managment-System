from django.db import models
from teacher.models import Teacher
from student.models import Student
from users.models import Users
from department.models import batch_no


# Create your models here.

class hod(models.Model):
	hod_name = models.OneToOneField(
	    'users.Users', on_delete=models.CASCADE, default=True)
	department_name = models.OneToOneField(
	    'department.department', on_delete=models.CASCADE, default=True)
	department_teacher = models.ManyToManyField('teacher.Teacher',  default=None, blank=True)
	department_students = models.ManyToManyField('student.Student', default=None, blank=True)
	
	def __str__(self):
		return str(self.department_name)