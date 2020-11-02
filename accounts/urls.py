from django.urls import path
#from .views import HomePageView
from . import views

urlpatterns = [
	path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('home/courses',views.courses, name='courses'),
    path('logout/', views.logOut, name='logout'),
    path('contactus/', views.contactus, name='contact')
]

