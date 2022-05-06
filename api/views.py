from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import basicSerializer, educationSerializer, employmentSerializer, referenceSerializer, skillSerializer
from .models import BasicInfo, Education, Employment, Referee, Skills

class BasicInfoView(APIView):
	def get_object(self):
		try:
			basic_obj = BasicInfo.objects.get(pk=1)
		except:
			basic_obj = BasicInfo()
		finally:
			return basic_obj

	def get(self, request):
		basic_obj = self.get_object()
		serialize_obj = basicSerializer(basic_obj)
		return Response(serialize_obj.data)

	def post(self, request):
		basic_obj = self.get_object()
		if basic_obj.id == None:
			serializer = basicSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
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
	def get(self, request):
		educations = Education.objects.all()
		serialize = educationSerializer(educations, many=True)
		return Response(serialize.data)

	def post(self, request):
		serializer = educationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EducationByID(APIView):
	def get_object(self, pk):
		return Education.objects.get(pk=pk)

	def get(self, request, pk):
		education_obj = self.get_object(pk)
		serialize_obj = educationSerializer(education_obj)
		return Response(serialize_obj.data)

	def put(self, request, pk):
		education_obj = self.get_object(pk)
		serialize_obj = educationSerializer(education_obj, data=request.data)
		if serialize_obj.is_valid():
			serialize_obj.save()
			return Response(serialize_obj.data, status=status.HTTP_200_OK)
		return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		education_obj = self.get_object(pk)
		education_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)

class EmploymentList(APIView):
	def get(self, request):
		employments = Employment.objects.all()
		serialize = employmentSerializer(employments, many=True)
		return Response(serialize.data)

	def post(self, request):
		serializer = employmentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmploymentByID(APIView):
	def get_object(self, pk):
		return Employment.objects.get(pk=pk)

	def get(self, request, pk):
		employment_obj = self.get_object(pk)
		serialize_obj = employmentSerializer(employment_obj)
		return Response(serialize_obj.data)

	def put(self, request, pk):
		employment_obj = self.get_object(pk)
		serialize_obj = employmentSerializer(employment_obj, data=request.data)
		if serialize_obj.is_valid():
			serialize_obj.save()
			return Response(serialize_obj.data, status=status.HTTP_200_OK)
		return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		employment_obj = self.get_object(pk)
		employment_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)

class ReferencesList(APIView):
	def get(self, request):
		references_obj = Referee.objects.all()
		serialize = referenceSerializer(references_obj, many=True)
		return Response(serialize.data)

	def post(self, request):
		serializer = referenceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReferenceByID(APIView):
	def get_object(self, pk):
		return Referee.objects.get(pk=pk)

	def get(self, request, pk):
		reference_obj = self.get_object(pk)
		serialize_obj = referenceSerializer(reference_obj)
		return Response(serialize_obj.data)

	def put(self, request, pk):
		reference_obj = self.get_object(pk)
		serialize_obj = referenceSerializer(reference_obj, data=request.data)
		if serialize_obj.is_valid():
			serialize_obj.save()
			return Response(serialize_obj.data, status=status.HTTP_200_OK)
		return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		reference_obj = self.get_object(pk)
		reference_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)

class SkillsList(APIView):
	def get(self, request):
		skills_obj = Skills.objects.all()
		serialize = skillSerializer(skills_obj, many=True)
		return Response(serialize.data)

	def post(self, request):
		serializer = skillSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillByID(APIView):
	def get_object(self, pk):
		return Skills.objects.get(pk=pk)

	def get(self, request, pk):
		skill_obj = self.get_object(pk)
		serialize_obj = skillSerializer(skill_obj)
		return Response(serialize_obj.data)

	def put(self, request, pk):
		skill_obj = self.get_object(pk)
		serialize_obj = skillSerializer(skill_obj, data=request.data)
		if serialize_obj.is_valid():
			serialize_obj.save()
			return Response(serialize_obj.data, status=status.HTTP_200_OK)
		return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		skill_obj = self.get_object(pk)
		skill_obj.delete()
		return Response( status=status.HTTP_204_NO_CONTENT)
