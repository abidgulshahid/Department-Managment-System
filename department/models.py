from django.db import models
from student.models import *
from teacher.models import *
from users.models import *




class batch_no(models.Model):
    batch_id = models.AutoField(primary_key=True)
    sec_batch = models.CharField(
        max_length=25, blank=True, null=True, help_text='pk')
    batch = models.CharField(max_length=256,null=True)
    section = models.CharField(
        max_length=10, help_text='Section Name Etc A,B,C etc', null=True)
    # students = models.ManyToManyField('student.Student')
    limit = models.SmallIntegerField(default=40, blank=True, null=True)
    depts = models.ForeignKey('department', on_delete=models.SET_NULL, default=None,blank=True,null=True)
    # student_batches = models.ForeignKey('student.Student', on_delete=models.SET_NULL, default=None,blank=True,null=True)
    std_br = models.ManyToManyField('student.Student')
    def save(self, *args, **kwargs):
        print(self.batch, self.section, self.sec_batch)
        if self.sec_batch is None or self.batch + "-" + self.section != str(self.sec_batch):
            self.sec_batch = str(self.batch) + "-" + str(self.section)
        super(batch_no, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('batch', 'section')

    def __str__(self):
        return self.sec_batch


class department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(
        "Department Name", max_length=255, help_text="Name of Department of Campus", unique=True)
    batches = models.ManyToManyField('batch_no',blank=True)

    department_hod = models.ForeignKey("users.Users", help_text="Current HOD of Department",
                                       name='department_hod', on_delete=models.CASCADE,blank=True, null=True,default=None)
    department_teachers = models.ManyToManyField(
        "teacher.Teacher", related_name='teachers_in_department', blank=True)
    department_students = models.ManyToManyField(
        "student.Student", related_name='students_in_department',blank=True)
    # batches = models.OneToOneField("batch_no",on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.department_name



class degree(models.Model):
    pass


class Semester(models.Model):
    SEMSESTER_CHOICES = (
        (1, "SPRING"),
        (2, "FALL"),
        (3, "SUMMER")
    )
    Semesters = (
        (1, '1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8')
    )
    semester = models.SmallIntegerField(choices=Semesters, name='semester',default='1')
    semester_season = models.SmallIntegerField(
        choices=SEMSESTER_CHOICES, name="semester_season")
    semester_year = models.IntegerField(name="semester_year")
    start_date = models.DateField(
        name="start_date", default=datetime.date.today)
    end_date = models.DateField(name="end_date", default=datetime.date.today)
    teachers_available = models.ManyToManyField(
        'teacher.Teacher', related_name="teachers_available", blank=True)
    batchess = models.ManyToManyField('batch_no')

    def __str__(self):
        return str(self.semester)


class subjects(models.Model):
    subject1 = models.CharField(max_length=100, default=None)
    subject2 = models.CharField(max_length=100, default=None)
    subject3 = models.CharField(max_length=100, default=None)
    subject4 = models.CharField(max_length=100, default=None)
    subject5 = models.CharField(max_length=100, default=None,blank=True)
    subject6 = models.CharField(max_length=100, default=None,blank=True)
    subject7 = models.CharField(max_length=100, default=None, blank=True)
    semester_subjects = models.ForeignKey("Semester", help_text="Semester", on_delete=models.CASCADE,blank=True, null=True,default=None)


class Attendence(models.Model):
    ATTENDANCE_STATES = (
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave')
    )
    class_date = models.DateField(
        name='class_date', blank=True, null=True, default=datetime.date.today)
    state = models.CharField(choices=ATTENDANCE_STATES, max_length=256, default='P')
    teacher  = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE, blank=True,  null=True)
    student = models.ManyToManyField('student.Student',blank=True)
    semester = models.ForeignKey('department.Semester', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.class_date)



class announcments(models.Model):
        msg = models.CharField(max_length=200, null=True)
        date = models.DateField(null=True)
     #   date = models.DateField(default=datetime.date.today)
        
        def __str__(self):
            return self.msg
