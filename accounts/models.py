from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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


class student_profile(models.Model):
   user =  models.OneToOneField(User, on_delete=models.CASCADE)
   semester = models.CharField(max_length=500, blank=True)
   batch_no = models.CharField(max_length=500, blank=True)
   city  =models.CharField(max_length=500, blank=True)
   dob = models.CharField(max_length=30, blank=True)



@receiver(post_save, sender=User)
def student_create_user_profile(sender,instance, created, **kwargs):
   if created:
      student_profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def student_save_user_profile(sender, instance, **kwargs):
   instance.student_profile.save()




class FeeChallan(models.Model):
    challan_no = models.CharField(max_length=300, default='123456777')
    due_date = models.DateField(auto_now=True)
    student = models.ForeignKey(User, verbose_name="Student Name", on_delete=models.CASCADE)
    admission_fee = models.FloatField(max_length=20, null=True, default=0)
    tution_fee = models.FloatField(max_length=20, null=True, default=0)
    Fine = models.FloatField(max_length=20, null=True, default=0)
    withholding_tax = models.FloatField(max_length=20, null=True, default=0)
    total_fee = models.FloatField(max_length=20, null=True, default=0)
    status = models.BooleanField(default=False)
    payment_date = models.DateField(auto_now=False, null=True)