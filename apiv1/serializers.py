from .models import (Student, Education, Internship, Project, Certificate, Summary, Skill, Language, CompetitiveExams,
                     Accomplishments)
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data['first_name'] = validated_data.get('first_name', '').title()
        validated_data['last_name'] = validated_data.get('last_name', '').title()
        user = User.objects.create_user(**validated_data)
        return user


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='enrollment_no.first_name')
    last_name = serializers.ReadOnlyField(source='enrollment_no.last_name')
    email = serializers.ReadOnlyField(source='enrollment_no.email')
    enrollment_no = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email'] + ['enrollment_no', 'branch', 'gender', 'dob', 'current_location',
                                                         'permanent_address', 'mobile_number', 'job_status']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class AccomplishmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accomplishments
        fields = '__all__'


class CompetitiveExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitiveExams
        fields = '__all__'
