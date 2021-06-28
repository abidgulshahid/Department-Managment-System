from os import name
from django.urls import path
#from .views import HomePageView
from . import views
urlpatterns = [
	path('',views.teacher_index,name='teacher'),  # Homepag

    path('<slug:teacher_id>/<int:choice>/Classes/', views.teacher_home, name="teacher_home"), #Student Batches
    path('<slug:classid>/Students', views.view_teacher_students, name='teacher_stud'), 
    path('info/<slug:student>/', views.each_student_info, name='each_student_info'),
    path('<slug:stud>/<slug:course>/<slug:teach>/', views.view_student_attendence, name='student_attendence'),

    # Assignment Routes


    path('<slug:class_id>/<slug:course>/', views.view_assignments_page, name='view_assignments_page'),
    path('/add/<slug:class_id>/<slug:course>/added/',views.add_assigment,name='add_assigment'),

   
    # get_assigment is used to view teacter's submitted Assignments and Delete is for to Delete Their Assignments
    path('get_assignments_data/', views.get_submitted_assignments, name='view_assignments'),
    path('delete_assignmet/<slug:ta>/deleted', views.delete_assignments, name='delete_assignments'),

    path('view_own_attendance',views.view_attendance,name='view_attendance'),

    path('promote/', views.promote_students, name='promote_students'),
    path('msgfromhod/',views.messages_from_hod, name='messages_from_hod'),
    # Marks Routes
    path('marks/<slug:stud>/<slug:course>/<slug:teach>/', views.teacher_view_marks, name='teacher_view_marks'),
    path('marks/<slug:stud>/<slug:teach>/take', views.take_marks, name='take_marks'),

    path('profile', views.teacher_profile, name='teacher_profiles'),

    path('profile/<slug:teacher>/update', views.update_profile, name='update_profile'),
    # path('teacher/<int:id>/teacher_view_students/',views.teacher_view_students, name='teacher_view_students'),
    path('logout/',views.logOut, name='logOut'),

]
