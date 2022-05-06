from rest_framework import serializers
from .models import BasicInfo, Education, Employment, Referee, Skills

class basicSerializer(serializers.ModelSerializer):
	class Meta:
		model = BasicInfo
		fields = '__all__'

class educationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = '__all__'

class employmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employment
		fields = '__all__'

class referenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Referee
		fields = '__all__'

class skillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skills
		fields = '__all__'
