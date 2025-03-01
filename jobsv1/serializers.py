from rest_framework import serializers
from .models import Job, ApplicationStatus


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(read_only=True, source='job', required=False)

    class Meta:
        model = ApplicationStatus
        fields = '__all__'
