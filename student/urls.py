from django.urls import path
#from .views import HomePageView
from . import views

urlpatterns = [
	path('',views.login,name='login'),
	path('register/', views.register, name = 'register'),
    path('home/', views.home, name='home'),
	path('logout/', views.logOut, name='logOut'),

]
