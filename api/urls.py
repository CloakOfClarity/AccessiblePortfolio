from . import views
from django.urls import path

urlpatterns = [
	path('education', views.EducationList.as_view()),
	path('education/<int:pk>', views.EducationByID.as_view()),
	path('employment', views.EmploymentList.as_view()),
	path('employment/<int:pk>', views.EmploymentByID.as_view()),
	path('skills', views.SkillsList.as_view()),
	path('skills/<int:pk>', views.SkillByID.as_view()),
	path('references', views.ReferencesList.as_view()),
	path('references/<int:pk>', views.ReferenceByID.as_view()),
]
