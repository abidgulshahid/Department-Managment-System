from django.urls import path
#from .views import HomePageView
from . import views
urlpatterns = [
		# path('',views.login,name='login'),
    path('hod_index/', views.hods, name='hods'),
    path('warning/<slug:listofstudents>/', views.wfhod, name='wfhod'),
    path('message/<slug:teacher>/', views.messagefhod, name='messagefhod'),
	path('logout/', views.logOut, name='logOut'),

]
