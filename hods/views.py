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
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.

def hod_login(request):
    pass


@login_required(login_url='login')
def hods(request):
    if request.user.is_superuser:
        students = Student.objects.all()
        student_counts = students.count()
        teachers = Teacher.objects.all().count()
        courses = Course.objects.all().count()
        for s in students:
            attendance = s.attendance_set.all().count()
            print(attendance)
        dep = Dept.objects.filter()
        for d in dep:
            s = d.teacher_set.all()
            print(s)
    
        res = {
            'total': int(student_counts)
        }
  
        context  = {'students':student_counts, 'teachers':teachers, 'courses':courses, 'dep':dep, 'los':students}
        return render(request, 'hod_index.html',context)
    else:
        return HttpResponse("<h2 style='color:red;'>Your Not Autorized To View This Page. </h2><p> Please Contact the Administrator</p>")


@login_required(login_url='login')
def wfhod(request,listofstudents):
    student = Student.objects.get(USN=listofstudents)
    warning_from = request.user.username
    warning_message = "Dear, "+student+" Warning: Apki Attendance Low hain Kindly Ap Apni Attedance Sahi Karay Warna Drop Hgy"

    query = warning.objects.create(warning_from=warning_from,warning_message=warning_message, student=student)
    if query:
        return HttpResponse("Warning From HOD Sent to "+str(query))
    else:
        return HttpResponse("ERROR")

def logOut(request):
    auth_logout(request)
    return redirect('login')
