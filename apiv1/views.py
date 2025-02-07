from .serializers import (StudentSerializer, EducationSerializer, InternshipSerializer, ProjectSerializer,
                          CertificateSerializer, UserSerializer, SkillSerializer, SummarySerializer, LanguageSerializer)
from .models import Student, Education, Internship, Project, Certificate, Skill, Summary, Language
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework import generics


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class StudentListCreateView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student.objects.filter(enrollment_no=self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(enrollment_no=self.request.user.username)


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student.objects.filter(enrollment_no=self.request.user.username)


class EducationListCreateView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Education.objects.filter(student__enrollment_no=self.request.user.username)


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Education.objects.filter(student__enrollment_no=self.request.user.username)


class InternshipListCreateView(generics.ListCreateAPIView):
    serializer_class = InternshipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Internship.objects.filter(student__enrollment_no=self.request.user.username)


class InternshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InternshipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Internship.objects.filter(student__enrollment_no=self.request.user.username)


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(student__enrollment_no=self.request.user.username)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(student__enrollment_no=self.request.user.username)


class CertificateListCreateView(generics.ListCreateAPIView):
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Certificate.objects.filter(student__enrollment_no=self.request.user.username)


class CertificateDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Certificate.objects.filter(student__enrollment_no=self.request.user.username)


class SkillListCreateView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Skill.objects.filter(student__enrollment_no=self.request.user.username)


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Skill.objects.filter(student__enrollment_no=self.request.user.username)


class SummaryListCreateView(generics.ListCreateAPIView):
    serializer_class = SummarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Summary.objects.filter(student__enrollment_no=self.request.user.username)


class SummaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SummarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Summary.objects.filter(student__enrollment_no=self.request.user.username)


class LanguageListCreateView(generics.ListCreateAPIView):
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Language.objects.filter(student__enrollment_no=self.request.user.username)


class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Language.objects.filter(student__enrollment_no=self.request.user.username)
