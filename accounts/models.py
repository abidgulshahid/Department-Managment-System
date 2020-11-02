from django.db import models
from datetime import datetime
# Create your models here.


class BSCS(models.Model):

	class_schedule = models.CharField(max_length=200,null=True)
	course_work = models.CharField(max_length=200,null=True)
	sem = models.CharField(max_length=10,null=True)
	subject_teacher = models.CharField(max_length=200,null=True)

	def __str__(self):
            return self.course_work


class announcments(models.Model):
        msg = models.CharField(max_length=200, null=True)
        date = models.DateField(null=True)
     #   date = models.DateField(default=datetime.date.today)
        
        def __str__(self):
            return self.msg



class students_courses(models.Model):
	pass

