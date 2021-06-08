from django.urls import path
#from .views import HomePageView
from . import views
urlpatterns = [
	path('',views.teacher_index,name='teacher'),
    path('<slug:teacher_id>/<int:choice>/Classes/', views.teacher_home, name="teacher_home"),
    path('<slug:classid>/Students', views.view_teacher_students, name='teacher_stud'),
    path('info/<slug:student>/', views.each_student_info, name='each_student_info'),
    path('<slug:stud>/<slug:teach>/', views.view_student_attendence, name='student_attendence'),

    path('<slug:s>/<slug:t>/', views.view_assignments_page, name='view_assignments_page'),

    path('<slug:t>/',views.add_assigment,name='add_assigment'),

    path('marks/<slug:stud>/<slug:teach>/', views.teacher_view_marks, name='teacher_view_marks'),
    path('marks/<slug:stud>/<slug:teach>/take', views.take_marks, name='take_marks'),
    path('profile', views.teacher_profile, name='teacher_profiles'),
    path('profile/<slug:teacher>/update', views.update_profile, name='update_profile'),
    # path('teacher/<int:id>/teacher_view_students/',views.teacher_view_students, name='teacher_view_students'),
    path('logout/',views.logOut, name='logOut'),


]
