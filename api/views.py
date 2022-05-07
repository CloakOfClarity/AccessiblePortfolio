from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import basicSerializer, educationSerializer, employmentSerializer, referenceSerializer, skillSerializer
from .models import BasicInfo, Education, Employment, Referee, Skills

class BasicInfoView(APIView):
# This class provides endpoints to get and set the user's basic information.

	def get_object(self):
		try:
# Check if the user has previously provided any basic information
			basic_obj = BasicInfo.objects.get(pk=1)
		except:
# If the answer is no, return an empty BasicInfo object
			basic_obj = BasicInfo()
		finally:
# Return the result
			return basic_obj

	def get(self, request):
# Use the get_object() function to query the database
		basic_obj = self.get_object()
		serialize_obj = basicSerializer(basic_obj)
		return Response(serialize_obj.data)

	def post(self, request):
# Use the get_object() function to query the database
		basic_obj = self.get_object()
# If no basic information has previously been saved, the ID of the returned object will be null.
		if basic_obj.id == None:
# In this case, the data will need to be created.
			serializer = basicSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
# Since there is already data in the database, it should be updated with the new information.
			serialize_obj = basicSerializer(basic_obj, data=request.data)
			if serialize_obj.is_valid():
				serialize_obj.save()
				return Response(serialize_obj.data, status=status.HTTP_200_OK)
			return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

"""
This function required only for testing.

	def delete(self, request):
		basic_obj = self.get_object()
		basic_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)
"""

class EducationList(APIView):
# This class provides endpoints to get and create the user's education

	def get(self, request):
# Retrieve a list of all education
		educations = Education.objects.all()
		serialize = educationSerializer(educations, many=True)
		return Response(serialize.data)

	def post(self, request):
# Create a new education with the specified data
		serializer = educationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EducationByID(APIView):
# This class provides endpoints to get, update and delete a single education entry

	def get_object(self, pk):
# A function to be used by the get, put and delete functions to locate the specified entry
		return Education.objects.get(pk=pk)

	def get(self, request, pk):
# Get the details for the specified education
		education_obj = self.get_object(pk)
		serialize_obj = educationSerializer(education_obj)
		return Response(serialize_obj.data)

	def put(self, request, pk):
# Update the specified education with the information in request.data
		education_obj = self.get_object(pk)
		serialize_obj = educationSerializer(education_obj, data=request.data)
		if serialize_obj.is_valid():
			serialize_obj.save()
			return Response(serialize_obj.data, status=status.HTTP_200_OK)
		return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
# Delete the specified education
		education_obj = self.get_object(pk)
		education_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)

class EmploymentList(APIView):
# This class provides endpoints to get and create the user's employment

	def get(self, request):
# Retrieve a list of all education
		employments = Employment.objects.all()
		serialize = employmentSerializer(employments, many=True)
		return Response(serialize.data)

	def post(self, request):
# Create a new employment with the specified data
		serializer = employmentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmploymentByID(APIView):
# This class provides endpoints to get, update and delete a single employment entry

	def get_object(self, pk):
# A function to be used by the get, put and delete functions to locate the specified entry
		return Employment.objects.get(pk=pk)

	def get(self, request, pk):
# Get the details for the specified employment
		employment_obj = self.get_object(pk)
		serialize_obj = employmentSerializer(employment_obj)
		return Response(serialize_obj.data)

	def put(self, request, pk):
# Update the specified employment with the information in request.data
		employment_obj = self.get_object(pk)
		serialize_obj = employmentSerializer(employment_obj, data=request.data)
		if serialize_obj.is_valid():
			serialize_obj.save()
			return Response(serialize_obj.data, status=status.HTTP_200_OK)
		return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
# Delete the specified employment
		employment_obj = self.get_object(pk)
		employment_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)

class ReferencesList(APIView):
# This class provides endpoints to get and create the user's references

	def get(self, request):
# Retrieve a list of all references
		references_obj = Referee.objects.all()
		serialize = referenceSerializer(references_obj, many=True)
		return Response(serialize.data)

	def post(self, request):
# Create a new reference with the specified data
		serializer = referenceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReferenceByID(APIView):
# This class provides endpoints to get, update and delete a single reference entry

	def get_object(self, pk):
# A function to be used by the get, put and delete functions to locate the specified entry
		return Referee.objects.get(pk=pk)

	def get(self, request, pk):
# Get the details for the specified reference
		reference_obj = self.get_object(pk)
		serialize_obj = referenceSerializer(reference_obj)
		return Response(serialize_obj.data)

	def put(self, request, pk):
# Update the specified reference with the information in request.data
		reference_obj = self.get_object(pk)
		serialize_obj = referenceSerializer(reference_obj, data=request.data)
		if serialize_obj.is_valid():
			serialize_obj.save()
			return Response(serialize_obj.data, status=status.HTTP_200_OK)
		return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
# Delete the specified reference
		reference_obj = self.get_object(pk)
		reference_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)

class SkillsList(APIView):
# This class provides endpoints to get and create the user's skills

	def get(self, request):
# Retrieve a list of all skills
		skills_obj = Skills.objects.all()
		serialize = skillSerializer(skills_obj, many=True)
		return Response(serialize.data)

	def post(self, request):
# Create a new skill with the specified data
		serializer = skillSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillByID(APIView):
# This class provides endpoints to get, update and delete a single skill entry

	def get_object(self, pk):
# A function to be used by the get, put and delete functions to locate the specified entry
		return Skills.objects.get(pk=pk)

	def get(self, request, pk):
# Get the details for the specified skill
		skill_obj = self.get_object(pk)
		serialize_obj = skillSerializer(skill_obj)
		return Response(serialize_obj.data)

	def put(self, request, pk):
# Update the specified skill with the information in request.data
		skill_obj = self.get_object(pk)
		serialize_obj = skillSerializer(skill_obj, data=request.data)
		if serialize_obj.is_valid():
			serialize_obj.save()
			return Response(serialize_obj.data, status=status.HTTP_200_OK)
		return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
# Delete the specified skill
		skill_obj = self.get_object(pk)
		skill_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)
