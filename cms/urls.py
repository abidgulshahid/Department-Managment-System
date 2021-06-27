"""test_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *
from student.urls import *

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls',
                                   'jet-dashboard')), 
    path('api/restapi/', include('department.urls'))  ,

    path('', index, name="index"),
    path('login/',include('users.urls'), name='users'),
    path('about/', about, name='about'),
    path('contact/', contact, name= 'contact'),
    path('teacher/', include('teacher.urls'),name="Teacher"),
    path('student/', include('student.urls'),name="Student"),
    path('hod/',include('hods.urls'), name='hods'),
    path('department/cs', computer, name='computer' ),
    path('department/ps', political, name='political' ),
    path('department/math', math, name='math' ),
    path('department/admissions', admissions,name='admissions'),
    path('superuser/admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'CMS Admin Portal'
admin.site.site_title = "CMS"
admin.site.index_title = "Welcome to CMS Admin Portal"
