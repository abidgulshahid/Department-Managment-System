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
    path('view_assignments_page/<slug:t>/', views.view_assignments_page, name='view_assignments_page'),
    path('<slug:assi>/added',views.add_assigment,name='add_assigment'),
    path('get_assignments_data/<slug:t>/', views.view_assignments, name='view_assignments'),
    path('delete_assignmet/<slug:ta>/', views.delete_assignments, name='delete_assignments'),

    path('promote/', views.promote_students, name='promote_students'),

    # Marks Routes
    path('marks/<slug:stud>/<slug:course>/<slug:teach>/', views.teacher_view_marks, name='teacher_view_marks'),
    path('marks/<slug:stud>/<slug:teach>/take', views.take_marks, name='take_marks'),

    path('profile', views.teacher_profile, name='teacher_profiles'),
    path('profile/<slug:teacher>/update', views.update_profile, name='update_profile'),
    # path('teacher/<int:id>/teacher_view_students/',views.teacher_view_students, name='teacher_view_students'),
    path('logout/',views.logOut, name='logOut'),


]
