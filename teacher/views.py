from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from department.models import *
from student.models import *
from users.models import Users
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
import datetime
# from hods.models import hod
from .models import Teacher, teacher_assignnment
# Create your views here.

@login_required(login_url='login')
def teacher_index(request):
    teacher1 = get_object_or_404(Teacher, user=request.user.id)
    ass = Assign.objects.filter(teacher=request.user.teacher)
    for x in ass:
        print(dir(x))
        print(x.assigntime_set.all())

    return render(request, 'teacher.html', {'teacher1': ass, 't':teacher1})
    # t =Assign.objects.filter(teacher_id=request.user.teacher).all()
    # print(dir(t))

    # for a in t:
        # print(a.teacher)
        # print('Courses:',a.course)
        # s = a.class_id.student_set.all()
        # print(s)

    # s = Student.objects.get(USN=t)
    # c = Class.objects.get(student=s)

    # context = {'teacher': t,'s':'s'}
    # return render(request, 'teacher.html', context)
@login_required(login_url='login')
def teacher_home(request, teacher_id, choice):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_students.html', {'teacher': teacher, 'choice': choice})


@login_required(login_url='login')
def view_teacher_students(request, classid):
    print(classid)
    teach = Teacher.objects.get(user=request.user.id)
    print(teach)
    ass = Assign.objects.get(id=classid)
    for x in ass.class_id.student_set.filter():
        print(dir(x))


    return render(request, 'teacher_stud.html', {'s':ass,'teach':teach})


@login_required(login_url='login')
def each_student_info(request,student):
    t  = Teacher.objects.get(user=request.user.id)
    assi = Assign.objects.get(teacher = t)
    attendance = Attendance.objects.filter(assign=assi)
    # for a in attendance:
    #     print(dir(a))
    #     print(dir(a.assign))
    student = Student.objects.filter(USN=student)
    for st in student:
        at = st.attendance_set.filter(assign=assi)
    # each_mark = Marks.objects.filter(student=st)
    # print(each_mark)
    return render(request,'each_student_info.html', {"student":st,'at':at,'assi':assi})


# def teacher_view_students(request,id):
#     std = Student.objects.get(pk=request.user.id)
#     print('asdas',std)
#     context = {'std':std}
#     return render(request,'teacher_students.html', context)
@login_required(login_url='login')
def teacher_profile(request):  
    teacher = get_object_or_404(Teacher, user=request.user.id)
    context  = {'teacher':teacher}
    print(dir(teacher))
    print(dir(teacher.user))

    return render(request, 'teacher_profile.html', context)



def update_profile(request,teacher):
    if request.method== "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        update_query = get_object_or_404(Users, teacher=teacher)
        update_query.first_name = fname
        update_query.last_name = lname
        if email in update_query.email:
            return HttpResponse("Email Already Existed")
        update_query.email = email
        update_query.save()
    
        return HttpResponse('UPDATED '+str(teacher))



@login_required(login_url='login')
def view_student_attendence(request,stud,teach):
    today = datetime.date.today()
    assi = Assign.objects.get(teacher_id=teach)
    student = Student.objects.get(USN=stud)

    if Attendance.objects.filter(assign=assi, student=student, attendance_date=today).exists():
        print ("Already Exist")
        return HttpResponse("Already TAKE the attendence")

    else:
        att = Attendance.objects.create(assign=assi, student=student, attendance_date=today)
        att.save()
    

    context  = {"stud":'Attendence Taken','student':student}
    return render(request, 'teacher_stud.html', context)
    
@login_required(login_url='login')
def teacher_view_marks(request,stud,teach):
    today = datetime.date.today()
    teach = Teacher.objects.get(user=request.user.id)
    student = Student.objects.get(USN=stud)
    std_course = StudentCourse.objects.filter()
    print(std_course)
    context = {"student":student, 'teacher':teach}

    return render(request, 'teacher_students_marks.html',context)

@login_required(login_url='login')
def take_marks(request,stud,teach):

    if request.method== "POST":
        today = datetime.date.today()
        assi = Assign.objects.get(teacher_id=teach)
        student = Student.objects.get(USN=stud)
        type = request.POST.get('type')
        marks= request.POST.get('marks')
        today = datetime.date.today()
        # tm = Marks.objects.create(assign=assi, student=student,marking_date=today, name=type, marks1=marks)
        return HttpResponse("CREATED")



@login_required(login_url='login')
def view_assignments_page(request):
    teacher = get_object_or_404(Teacher, user=request.user.id)
    context= {"t":teacher}
    return render(request, 'add_assignment.html', context)

@login_required(login_url='login')
def add_assigment(request,t):
    if request.method == "POST":
        today = datetime.date.today()
        assignment = request.POST.get('assignment')
        teacher = request.POST.get('teacher')
        teacher_assignnment.objects.create(assign=teacher, assignment=assignment, assignment_date=today)
        return HttpResponse("Assignment Created")




@login_required(login_url='login')
def logOut(request):
    auth_logout(request)
    return redirect('login')

