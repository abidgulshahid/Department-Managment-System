from django.urls import path
#from .views import HomePageView
from . import views
urlpatterns = [
	path('',views.login,name='login'),
    path('admin/dashboard', views.admin_dashboard, name='admin_dashboard'),
	# path('register/', views.register, name = 'register'),
    # path('home/', views.home, name='home'),
	# path('home/courses', views.courses, name='courses'),
	# path('home/attendence',views.show_attendence, name='show_attendence'),
	# path('home/fee',views.fee, name='fee'),
	path('logout/', views.logOut, name='logOut'),

]
