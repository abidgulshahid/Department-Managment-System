from django.shortcuts import render,redirect
from .models import announcments

def index(request):
    announce = announcments.objects.all().order_by('msg')
    context = {"announcments": announce}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def computer(request):
    return render(request, 'computer_science.html')

def bscomp(request):
    return render(request, 'bscom.html')

def faculty(request):
    return render(request, 'faculty.html')


def math(request):
    return render(request, 'math.html')

def political(request):
    return render(request,'political.html')


def admissions(request):
    return render(request, 'admissions.html')