from django.db import models
from users.models import Users
from django.contrib.auth.models import Group

# Create your models here.
QUALIFICATIONS = (
    (1, 'Bachelors'),
    (2, 'Masters'),
    (3, 'Doctrate')
)

class Teacher(models.Model):
    t = models.OneToOneField('users.Users', on_delete=models.CASCADE, default=None, blank=True,null=True)
    highest_qualification = models.SmallIntegerField(choices=QUALIFICATIONS, name='highest_qualification', null=True)
    
    # department = models.CharField(max_length=10, null=True)
    nu_email = models.CharField(max_length=100,blank=True)

    # @classmethod
    # def create(cls, user=None, nu_email=None, **kwargs):
    #     if t is None:
    #         username = None
    #         password = None
    #
    #         username = kwargs['username']
    #         password = kwargs['password']
    #
    #         u = Users.create(username=username, password=password,
    #                         is_teacher=True, is_employee=True)
    #         t = u
    #
    #     t = cls(user=Users, nu_email=nu_email)
    #     t.save()
    #     # t.groups.add(Group.objects.get(name='teacher_group'))
    #     return t
    #
    # # def save(self, *args, **kwargs):
    # #     created = self.id is None
    # #     super(YourModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.t.username

    # class Meta:
    #     ordering = ('-pk',)
    #
    # def __unicode__(self):
    #     return u'%s' % self.pk

