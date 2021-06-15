from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
import random
from users.models import Users
from django.http import HttpResponse


class UserAPIView(APIView):
    def get(self, _):
        users = Users.objects.all()
        user = random.choice(users)
        return response ({
            'is_teacher' : 'True'
        })
