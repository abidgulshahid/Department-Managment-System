from io import open_code
from django.db import models
from student.models import *
from teacher.models import *
from users.models import Users
import datetime
import math
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime

time_slots = (
    ('7:30 - 8:30', '7:30 - 8:30'),
    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)

DAYS_OF_WEEK = (
    ('Monday-Wednesday', 'Monday-Wednesday'),
    ('Thursday-Sat', 'Thursday-Sat'),
    ('Monday-Tuesday', 'Monday-Tuesday'),
    ('Thursday-Friday', 'Thursday-Friday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


test_name = (
    ('Internal test 1', 'Internal test 1'),
    ('Internal test 2', 'Internal test 2'),
    ('Mid', 'Mid'),
    ('Terminal Exam', 'Terminal Exam'),
)



class Dept(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Course(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50, default='X')

    def __str__(self):
        return self.name


class Class(models.Model):
    # courses = models.ManyToManyField(Course, default=1)
    id = models.CharField(primary_key='True', max_length=50)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    sem = models.IntegerField()

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        d = Dept.objects.get(name=self.dept)
        return '%s : %d %s' % (d.name, self.sem, self.section)


class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'class_id', 'teacher'),)

    def __str__(self):
        cl = Class.objects.get(id=self.class_id_id)
        cr = Course.objects.get(id=self.course_id)
        te = Teacher.objects.get(id=self.teacher_id)
        return '%s : %s : %s' % (te.name, cr.shortname, cl)



class AssignTime(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    period = models.CharField(max_length=500, choices=time_slots, default='11:00 - 11:50')
    day = models.CharField(max_length=150, choices=DAYS_OF_WEEK)

    def __str__(self):
        return '%s %s %s' % (self.assign.course, self.period, self.day)

class Attendance(models.Model):
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    student=  models.ForeignKey('student.Student', on_delete=models.CASCADE)
    attendance_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s " % (self.assign.course, self.student)

    class Meta:
        ordering = ['-attendance_date']


class Markss(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    student=  models.ForeignKey('student.Student', on_delete=models.CASCADE)
    marking_date = models.DateField()
    name = models.CharField(max_length=50, choices=test_name, default='Internal test 1')
    marks1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])



    @property
    def total_marks(self):
        if self.name == 'Semester End Exam':
            return 100
        return 20

    def __str__(self):
        return "%s %s %s " % (self.assign.teacher,self.student, self.name)



class StudentCourse(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('student', 'course'),)
        verbose_name_plural = 'Marks'



    def get_cie(self):
        marks_list = self.marks_set.all()
        m = []
        for mk in marks_list:
            m.append(mk.marks1)
        cie = math.ceil(sum(m[:5]) / 2)
        return cie

class Marks(models.Model):
    studentcourse = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=test_name, default='Internal test 1')
    marks1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        unique_together = (('studentcourse', 'name'),)

    @property
    def total_marks(self):
        if self.name == 'Semester End Exam':
            return 100
        return 20


class MarksClass(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=test_name, default='Internal test 1')
    status = models.BooleanField(default='False')

    class Meta:
        unique_together = (('assign', 'name'),)

    @property
    def total_marks(self):
        if self.name == 'Semester End Exam':
            return 100
        return 20


class Semester(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mark  = models.ForeignKey(Markss, on_delete=models.CASCADE)


