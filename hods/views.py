from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from department.models import *
from student.models import Student
from users.models import Users
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from teacher.views import teacher_index
from teacher.urls import *
from department.models import *
from hods.models import *
# Create your views here.


def hods(request):
    if request.user.is_admin:
        dept = hod.objects.get(hod_name=request.user.id)
        students = Student.objects.filter(hod=dept)
        teachers = Teacher.objects.filter(hod=dept)
        batches = batch_no.objects.filter(batch_depts=department.objects.get(hod=dept))
        for teacher in teachers:
            print(dir(teacher))

    else:
        dept = "User Not Found"
    context = {'dept': dept, 'teacher': teacher, 'students': students}
    return render(request, 'hod_index.html', context)


def logOut(request):
    auth_logout(request)
    return redirect('login')
