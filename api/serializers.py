from rest_framework import serializers
from .models import Education, Employment, Skills

class educationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = '__all__'

class employmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employment
		fields = '__all__'

class skillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skills
		fields = '__all__'
