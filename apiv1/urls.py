from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (RegisterUserView, StudentListCreateView, StudentDetailView, EducationListCreateView,
                    EducationDetailView, InternshipListCreateView, InternshipDetailView, ProjectListCreateView,
                    ProjectDetailView, CertificateListCreateView, CertificateDetailView, SkillDetailView,
                    SummaryListCreateView, SummaryDetailView, SkillListCreateView, LanguageDetailView,
                    LanguageListCreateView, AddStudentsView, AccomplishmentsListCreateView, AccomplishmentDetailView,
                    CompetitiveExamsDetailView, CompetitiveExamsListCreateView)
from django.urls import path

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add_students/', AddStudentsView.as_view(), name='add_students'),
]

urlpatterns += [
    path('student/', StudentListCreateView.as_view(), name='add or view student'),
    path('student/<pk>/', StudentDetailView.as_view(), name='student'),

    path('education/', EducationListCreateView.as_view(), name='add or view education'),
    path('education/<pk>/', EducationDetailView.as_view(), name='education'),

    path('internship/', InternshipListCreateView.as_view(), name='add or view internship'),
    path('internship/<pk>/', InternshipDetailView.as_view(), name='internship'),

    path('project/', ProjectListCreateView.as_view(), name='add or view project'),
    path('project/<pk>/', ProjectDetailView.as_view(), name='project'),

    path('certificate/', CertificateListCreateView.as_view(), name='add or view certificate'),
    path('certificate/<pk>/', CertificateDetailView.as_view(), name='certificate'),

    path('skill/', SkillListCreateView.as_view(), name='add or view skill'),
    path('skill/<pk>/', SkillDetailView.as_view(), name='skill'),

    path('language/', LanguageListCreateView.as_view(), name='add or view language'),
    path('language/<pk>/', LanguageDetailView.as_view(), name='language'),

    path('summary/', SummaryListCreateView.as_view(), name='add or view summary'),
    path('summary/<pk>/', SummaryDetailView.as_view(), name='summary'),

    path('accomplishments/', AccomplishmentsListCreateView.as_view(), name='add or view accomplishments'),
    path('accomplishments/<pk>/', AccomplishmentDetailView.as_view(), name='accomplishment'),

    path('competitive_exams/', CompetitiveExamsListCreateView.as_view(), name='add or view competitive_exams'),
    path('competitive_exams/<pk>/', CompetitiveExamsDetailView.as_view(), name='competitive_exam'),
]
