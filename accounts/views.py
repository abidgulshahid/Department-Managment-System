from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import createuserform
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import student_profiles
from django.db import transaction


def index(request):
	if request.user.is_authenticated:
		return redirect('home')
	announce = announcments.objects.all()
	context = {"announcments": announce}
	return render(request, 'index.html', context)


def register(request):
    form = createuserform()
    if request.method == 'POST':
    	form = createuserform(request.POST)
    	if form.is_valid():
    		form.save()
    		username = form.cleaned_data.get('username')
    		messages.success(request, 'Account Created for '+username)
    		return redirect('login')

    context = {'form': form}
    print(context)
    return render(request, 'register.html', context)


def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth_login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)


@login_required(login_url='login')
def home(request):
	global fee
	all_data = BSCS.objects.all()
	announce = announcments.objects.all()
	try:
		fee = FeeChallan.objects.get(student=request.user.id)
	except FeeChallan.DoesNotExist:
		fee = "FEE Currently Not Available For You"
	context = {"DATA": all_data, "announcments": announce, 'fee': fee}

	return render(request, 'home.html', context)


@login_required(login_url='login')
def courses(request):
	all_data = BSCS.objects.all()
	context = {"DATA": all_data}
	return render(request, 'courses.html', context)


@login_required(login_url='login')
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
            userform = createuserform(request.POST, instance=request.user)
            print(dir(request.user))
            profiles = student_profiles(
                request.POST, instance=request.user.student_profile)
            if userform.is_valid() and profiles.is_valid():
                userform.save()
                profiles.save()
                messages.success(request, "PROFILE UPDATED")
                return redirect('courses')
            else:
                messages.error(
                    request, "Please Correct the following Error Below"+str(profiles))
    else:
        userform = createuserform(instance=request.user)
        profiles = student_profiles(instance=request.user.student_profile)
    return render(request, 'edit_profile.html', {'userform': userform, 'profiles': profiles})


def admin_login(request):
	pass
	# 	if request.user.is_authenticated:
	# 		return redirect('home')
	# else:
	# 	if request.method == 'POST':
	# 		username = request.POST.get('username')
	# 		password =request.POST.get('password')

	# 		user = authenticate(request, username=username, password=password)
			


	# 		if user is not None:
	# 			auth_login(request, user)
	# 			return redirect('home')
	# 		else:
	# 			messages.info(request, 'Username OR password is incorrect')

	# 	context = {}
	# 	return render(request, 'login.html', context)



def logOut(request):
	auth_logout(request)
	return redirect('login')



def about(request):
 	return render(request, 'about.html')


def contact(request):
	return render(request, 'contact.html')






