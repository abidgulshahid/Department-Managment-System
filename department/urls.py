from django.urls import path
#from .views import HomePageView
from . import views

from .views import UserAPIView
urlpatterns = [
	path('user', UserAPIView.as_view()),


]
