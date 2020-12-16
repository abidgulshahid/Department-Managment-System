from django.urls import path
#from .views import HomePageView
from . import views
urlpatterns = [
	path('',views.teacher_index,name='teacher'),
    path('logout/',views.logOut, name='logOut'),


]
