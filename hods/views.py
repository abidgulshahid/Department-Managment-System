from django.contrib.auth.models import User
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
from teacher.views import teacher_index
from teacher.urls import *
from department.models import *
from hods.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import datetime

# Create your views here.

def hod_login(request):
    pass


@login_required(login_url='login')
def hods(request):
    if request.user.is_superuser:
        students = Student.objects.all()
        student_counts = students.count()
        perc_atnd = student_counts / 48 * 100
        each_attendance = Attendance.objects.filter(student__in=students)
        teachers = Teacher.objects.all()
        each_teacher_attendance = Teacher_Attendance.objects.filter(teacher__in=teachers)
        for e in each_teacher_attendance:
            print(dir(e))
            print(e)

        teacher_counts = teachers.count()
        courses = Course.objects.all().count()

        for eta in teachers:
            each_teacher_attendances = eta.teacher_attendance_set.all().count()

        for s in students:
            attendance = s.attendance_set.all().count()
            warning_counts = s.warning_set.all().count()

            print(attendance)
        dep = Dept.objects.filter()
        for d in dep:
            s = d.teacher_set.all()
            print(s)
    
        res = {
            'total': int(student_counts)
        }
  
        context  = {

            'students':student_counts,
            'warning_counts':warning_counts,
            'each_perc':int(perc_atnd), 
            'teacher_counts':teacher_counts ,
            'teachers':teachers, 
            'eta':each_teacher_attendance,
            'courses':courses, 
            'dep':dep, 
            'los':students
            
            }
        return render(request, 'hod_index.html',context)
    else:
        return HttpResponse("<h2 style='color:red;'>Your Not Autorized To View This Page. </h2><p> Please Contact the Administrator</p>")


@login_required(login_url='login')
def wfhod(request,listofstudents):
    student = Student.objects.get(USN=listofstudents)
    warning_from = request.user.username
    warning_message = request.POST.get('message')
    todays = datetime.date.today()

    query = warning.objects.create(warning_from=warning_from,warning_message=warning_message, student=student,warning_date=todays)
    if query:
        messages.success(request, "ASDASDS")    
        return HttpResponseRedirect(reverse('hods'))
    else:
        return HttpResponse("ERROR")


login_required(login_url='login')
def messagefhod(request,teacher):
    student = Teacher.objects.get(id=teacher)
    warning_from = request.user.username
    warning_message = request.POST.get('message')
    todays = datetime.date.today()

    query = messagetoteacher.objects.create(message_from=warning_from,message=warning_message, teacher=student,msg_date=todays)
    if query:
        messages.success(request, "ASDASDS")    
        return HttpResponseRedirect(reverse('hods'))
    else:
        return HttpResponse("ERROR")


login_required(login_url='login')
def teacher_attendance(request,teacher):
    today = datetime.date.today()
    admin = Users.objects.get(id=request.user.id)
    status= request.POST.get('status')
    teachr = Teacher.objects.get(id=teacher)
    if Teacher_Attendance.objects.filter(assign=admin, teacher=teachr,attendance_date=today).exists():
        print ("Already Exist")
        return HttpResponse("Already TAKE the attendence")

    else:
        att = Teacher_Attendance.objects.create(assign=admin, teacher=teachr, status=status, attendance_date=today)
        att.save()

    return HttpResponse('Attendance Taken'+str(admin))


    #Teacher_Attendance

login_required(login_url='login')
def Assign_classes(request):
    pass




def logOut(request):
    auth_logout(request)
    return redirect('login')
