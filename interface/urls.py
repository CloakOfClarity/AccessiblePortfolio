from . import views
from django.urls import path

urlpatterns = [
	path('', views.homePage, name='Home'),
	path('education', views.educationPage, name='Education'),
	path('employment', views.employmentPage, name='Employment'),
	path('skills', views.skillsPage, name='Skills'),
]
