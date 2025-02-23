from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .serializers import (StudentSerializer, EducationSerializer, InternshipSerializer, ProjectSerializer,
                          CertificateSerializer, UserSerializer, SkillSerializer, SummarySerializer, LanguageSerializer,
                          AccomplishmentsSerializer, CompetitiveExamsSerializer)
from .models import (Student, Education, Internship, Project, Certificate, Skill, Summary, Language, Accomplishments,
                     CompetitiveExams)
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
import csv
import io


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class StudentListCreateView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student.objects.select_related('enrollment_no').filter(enrollment_no=self.request.user.username)

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


class AddStudentsView(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    permission_classes = [AllowAny, ]

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        writer = csv.writer(response)
        writer.writerow(
            ['username', 'password', 'first_name', 'last_name', 'email', 'branch', 'Gender', 'DOB', 'Mobile Number']
        )
        return response

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')  # Get the uploaded file

        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = file.read().decode('utf-8')  # Decode the file
            csv_reader = csv.DictReader(io.StringIO(decoded_file))  # Read CSV
            csv_reader1 = csv.DictReader(io.StringIO(decoded_file))  # Read CSV

            users = []
            errors = []
            students = []

            for row in csv_reader:
                user_serializer = UserSerializer(data=row)  # Validate row

                if user_serializer.is_valid():
                    user_serializer.validated_data['password'] = make_password(user_serializer.validated_data['password'])
                    users.append(user_serializer.validated_data)
                else:
                    errors.append({"row": row, "errors": user_serializer.errors})

            User.objects.bulk_create([User(**data) for data in users])

            # Bulk create valid records
            for row in csv_reader1:
                row['enrollment_no'] = row['username']
                student_serializer = StudentSerializer(data=row)
                if student_serializer.is_valid():
                    students.append(student_serializer.validated_data)
                else:
                    errors.append({"row": row, "errors": student_serializer.errors})
            if errors:
                return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

            Student.objects.bulk_create([Student(**data) for data in students])

            return Response({"message": "CSV uploaded successfully", "users_added": len(users), "students_updated": len(students)},
                            status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AccomplishmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccomplishmentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Accomplishments.objects.filter(student__enrollment_no=self.request.user.username)


class AccomplishmentsListCreateView(generics.ListCreateAPIView):
    serializer_class = AccomplishmentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Accomplishments.objects.filter(student__enrollment_no=self.request.user.username)


class CompetitiveExamsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompetitiveExamsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CompetitiveExams.objects.filter(student__enrollment_no=self.request.user.username)


class CompetitiveExamsListCreateView(generics.ListCreateAPIView):
    serializer_class = CompetitiveExamsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CompetitiveExams.objects.filter(student__enrollment_no=self.request.user.username)

