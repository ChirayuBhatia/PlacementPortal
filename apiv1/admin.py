from django.contrib import admin
from .models import Student, Education, Internship, Project, Certificate


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_no',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('student', 'qualification', 'board_university')


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('student',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('student', 'project_name')
    search_fields = ('project_name',)
    list_filter = ('project_name',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('student', 'certificate_name')
    search_fields = ('certificate_name',)
    list_filter = ('certificate_name',)
