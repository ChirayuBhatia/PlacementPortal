from rest_framework import serializers
from .models import Job, ApplicationStatus


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = '__all__'

    def get_queryset(self):
        return ApplicationStatus.objects.filter(user=self.context['request'].user)
