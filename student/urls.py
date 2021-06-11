from django.urls import path
#from .views import HomePageView
from . import views
urlpatterns = [
		# path('',views.login,name='login'),
	path('register/', views.register, name = 'register'),
    path('home/', views.student, name='student'),
	path('home/courses', views.courses, name='courses'),
	path('home/show_assignment', views.show_attendance, name='show_assignment'),
	path('home/attendence',views.show_attendence, name='show_attendence'),
	path('home/result',views.result, name='marks'),
	path('home/fee',views.fee, name='fee'),
	path('home/profile',views.student_profile, name='student_profile'),
	path('home/profile/<slug:student>/update',views.update_student_profile, name='update_student_profile'),
	path('logout/', views.logout, name='logOut'),

]
