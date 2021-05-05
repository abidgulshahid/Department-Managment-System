from django.db import models
from teacher.models import Teacher
from student.models import Student
from users.models import Users


# Create your models here.

# class hod(models.Model):	
# 	id = models.AutoField(primary_key=True)
# 	hod_name = models.OneToOneField(
# 	    'users.Users', on_delete=models.CASCADE, default=True,limit_choices_to={'is_admin': True} , related_name="Head")
# 	department_name = models.OneToOneField(
# 	    'department.department', on_delete=models.CASCADE, default=True, related_name='NAME')
# 	department_teacher = models.ManyToManyField('teacher.Teacher',  default=None, blank=True , related_name="DT")
# 	department_students = models.ManyToManyField('student.Student', default=None, blank=True)
	
# 	def __str__(self):
# 		return str(self.department_name)