from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import student_profile


class createuserform(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','username','email']


class student_profiles(forms.ModelForm):
	class Meta:
		model = student_profile
		fields = ('semester','batch_no','city', 'dob')
