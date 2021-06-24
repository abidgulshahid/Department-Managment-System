from django.db import models
from users.models import Users
from department.models import *
# Create your models here.



class Student(models.Model):
    USN =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True,blank=True)
    class_id = models.ForeignKey('department.Class', on_delete=models.CASCADE, default=1)
    DOB = models.DateField(default='1998-01-01')

    def __str__(self):
        return self.name

