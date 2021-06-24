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

class warning(models.Model):
    warning_from  = models.CharField(max_length=200,null=True,blank=True)
    warning_message = models.CharField(max_length=3000,null=True,blank=True)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    warning_date = models.DateField()

    class Meta:
        ordering = ['-warning_date']

class messagetoteacher(models.Model):
    message_from  = models.CharField(max_length=200,null=True,blank=True)
    message = models.CharField(max_length=3000,null=True,blank=True)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE)
    msg_date = models.DateField()

    class Meta:
        ordering = ['-msg_date']
