from django.db import models
from datetime import datetime




class announcments(models.Model):
        msg = models.CharField(max_length=200, null=True)
        date = models.DateField(null=True)
     #   date = models.DateField(default=datetime.date.today)
        
        def __str__(self):
            return self.msg
