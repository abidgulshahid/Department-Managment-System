from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from department.models import *
from student.models import Student
from users.models import Users
from django.contrib.auth import logout as auth_logout
from .forms import StudentForm
# Create your views here.

def register(request):
	form = StudentForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('login')
			
	context = {'form': form}
	return render(request, 'register.html', context)



def login(request):
	if request.user.is_authenticated and request.user.is_student:
		return redirect('home')
	# else if:
	# 	return render(request, 'not_student.html')
	if request.user.is_authenticated and request.user.is_student:
		return redirect('home')
	elif request.user.is_authenticated and not  request.user.is_student:
		return render(request, 'thanks.html')
	else:
		if request.method == 'POST':
			email = request.POST.get('email')
			password = request.POST.get('password')

			user = authenticate(request, email=email, password=password)

			print ('---',dir(user))		
			if user.is_student == False:
				return render(request, 'thanks.html')

			elif user is not None:
				auth_login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

@login_required(login_url='login')
def home(request):
	global sem,sub, batches, user_info
	try:
		user_info = Student.objects.get(students=request.user)
	except:
		user_info = "Student Not Available"
#	print(dir(user_info))
	try:
		batches = batch_no.objects.get(student=Student.objects.get(students=request.user))
	except:
		batches = "Batches Not Available At the Moment"
	try:
		sem = Semester.objects.get(batchess=batches)
	except:
		sem = "Your are Not Assigned To any Semester"
	try:
		sub = subjects.objects.get(semester_subjects=sem)
	except:
		sub ="NO SUBJECTS"
	try:
		attendence = Attendence.objects.get(student=user_info)
	except:
		attendence = "NOT AVAILABLE AT THE MOMENT"
	print(attendence)
#	d = department.objects.get(batches=batch_no.objects.get(student=Student.objects.get(students=request.user))).first()
	context = {'u':user_info, 'b':batches,'sem':sem, 'sub':sub,'a':attendence}
	return render(request, 'home.html', context)

def logOut(request):
	auth_logout(request)
	return redirect('login')
