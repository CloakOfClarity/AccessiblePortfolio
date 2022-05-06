from django.shortcuts import render

def homePage(request):
	return render(request, 'home.html')

def educationPage(request):
	return render(request, 'education.html')

def employmentPage(request):
	return render(request, 'employment.html')

def referencesPage(request):
	return render(request, 'references.html')

def skillsPage(request):
	return render(request, 'skills.html')
