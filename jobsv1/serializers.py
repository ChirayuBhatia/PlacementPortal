from rest_framework import serializers
from .models import Job, ApplicationStatus


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = '__all__'
