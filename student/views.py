from teacher.models import teacher_assignnment
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from department.models import *
from student.models import Student
from users.models import Users
from hods.models import warning
from django.contrib.auth import logout as auth_logout
from .forms import StudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from teacher.views import teacher_index
from teacher.urls import *
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def register(request):
	form = StudentForm(request.POST)
	if form.is_valid():
		form.save()
		email = form.cleaned_data.get('email')
		messages.success(request, 'Account Created for '+email)
		return redirect('login')
			
	context = {'form': form}
	return render(request, 'register.html', context)



# def login(request):
# 	# if request.user.is_authenticated and request.user.is_student:
# 	# 	return redirect('home')
# 	# elif request.user.is_authenticated and request.user.is_admin:
# 	# 	return redirect('teacher')
	
# 	# elif request.user.is_authenticated and request.user.is_teacher:
# 	# 	pass

# 	# else:
# 	# 	print(request.user.is_authenticated)
# 	# 	return render(request,'login.html')
# 	# else if:
# 	# 	return render(request, 'not_student.html')
# 	# if request.user.is_authenticated and request.user.is_student:
# 	# 	return redirect('home')
# 	# elif request.user.is_authenticated and not  request.user.is_student:
# 	# 	return render(request, 'thanks.html')
# 	# else:
# 		if request.method == 'POST':
# 			email = request.POST.get('email')
# 			password = request.POST.get('password')
# 			try:
# 				user = authenticate(request, email=email, password=password)
# 				# print ('---',dir(user))	
# 				# print('========',dir(request.user))
# 				print("status: ", user.is_student)
# 				print("status: ", user.is_admin)
# 				print("status: ", user.is_superuser)

# 				if user.is_student and user is not None:
# 					auth_login(request, user)
# 					return redirect('home')
				
# 				elif user.is_superuser and user is not None:
# 					auth_login(request, user)
# 					return HttpResponseRedirect(reverse('admin:index'))
				
# 				elif user.is_admin==True and user is not None: 
# 					auth_login(request, user)
# 					return HttpResponseRedirect(reverse('teacher'))

# 				elif user.is_student == False  and user is not None:
# 					auth_login(request,user)
# 					return redirect('home') 
# 				# else:
# 				# 	return redirect('index')
# 				else:
# 					messages.info(request, 'Username OR password is incorrect')
# 			except:
# 				user = "Something Wrong"
# 		context = {'message':messages}
# 		return render(request, 'login.html', context)

@login_required(login_url='login')
def student(request):
	print(dir(request.user))
	if request.user.is_student:
		a= Student.add_to_class(str(request.user), value="ADDED")
		print(a)
	#print (std)
	global sem, batches, user_info
	try:
		user_info = Student.objects.get(students=request.user)
	except:
		user_info = "Student Not Available"
#	print(dir(user_info))
	try:
		batches = batch_no.objects.get(student=Student.objects.get(students=request.user))
	except:
		batches = "    \tYour not assigned to any batches"
	try:
		sem = Semester.objects.get(batchess=batches)
	except:
		sem = "  Your are Not Assigned To any Semester"

	try:
		attendence = Attendence.objects.get(student=user_info)
	except:
		attendence = "NOT AVAILABLE AT THE MOMENT"
#	d = department.objects.get(batches=batch_no.objects.get(student=Student.objects.get(students=request.user))).first()
	context = {'u':user_info, 'b':batches,'sem':sem,'a':attendence}
	return render(request, 'home.html', context)


@login_required(login_url='login')
def courses(request):
	student = Student.objects.get(user=request.user.id)
	course = Class.objects.get(student=student)
	ass = Assign.objects.filter(class_id=course)
	for a in ass:
		print(dir(a))
		for i in a.assigntime_set.all():
			print(i.day)
	context = {"course":ass, 'time':'ass_time'}
	return render(request, 'courses.html', context)

@login_required(login_url='login')
def show_attendance(request):

	student = Student.objects.get(user=request.user.id)

	course = Class.objects.get(student=student)
	assign = Assign.objects.filter(class_id = course)
	view_assignment = teacher_assignnment.objects.filter(assign__in=assign)

	context = {"view_assignment":view_assignment}
	return render(request, 'show_assignment.html', context)


@login_required(login_url='login')
def show_attendence(request):
	status = ''
	present = 0 
	absent = 0
	total_perc_attendance = 0
	attendence = Attendance.objects.filter(student_id=request.user.student)
	import datetime
	today = datetime.date.today()
	s  = Attendance.objects.filter(attendance_date=today)
	perc_attendance  = attendence.count()
	for sad in attendence:
		if sad.status == 'Absent':
			total_perc_attendance  = (perc_attendance -1) / 48 * 100 
			absent  = (perc_attendance -1) / 48 * 100 
		else:
			total_perc_attendance  = perc_attendance / 48 * 100 
			present  = perc_attendance / 48 * 100 


	print(s)

	if Attendance.objects.filter(attendance_date=today).exists():
		status  = "Present"
	else:
		status = "Absent "


	context = {'a': attendence, 'total_attendannce': int(total_perc_attendance), 'present':int(present), 'absent':int(absent)}
	return render(request, 'attendence.html', context)
	
@login_required(login_url='login')
def result(request):
	student = Student.objects.get(user=request.user.id)
	course = Class.objects.get(student=student)
	ass = Assign.objects.filter(class_id=course)	
	std_course = Markss.objects.filter(assign__in=ass, student=student)
	print(std_course)
	for std_x in std_course:
		print(std_x)

	# mk = Marks.objects.filter(student_id = request.user.student)

	# for m in mk:
	# 	m=m
	# 	print('marks', m.marks1)
	# 	print('teacher',m.assign.teacher, m.assign.course)


	context = {'mark':std_course}
	return render(request,'marks.html', context)

@login_required(login_url='login')
def student_profile(request):
	student = Student.objects.get(user=request.user.id)

	print(dir(student))
	print(student.USN)
	context = {'student':student}
	return render(request, "student_profile.html", context)

@login_required(login_url='login')
def update_student_profile(request, student):
	if request.method == "POST":
		print(student)
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		username = request.POST.get('username')
		email = request.POST.get('email')
		update_query = get_object_or_404(Users, student=student)
		update_query.first_name = fname
		update_query.last_name = lname
		if email in update_query.email:
			return HttpResponse("Email Already Existed")
		update_query.email = email
		update_query.save()
		
		return HttpResponse("HACKED")




@login_required(login_url='login')
def upload_assignment(request):
	pass

@login_required(login_url='login')
def show_warnings(request):
	student = Student.objects.get(user=request.user.id)
	warnings = warning.objects.filter(student=student)
	context={"warning":warnings}
	return render(request, 'warnings.html', context)

def fee(request):
	pass



def logout(request):
	auth_logout(request)
	return redirect('login')
