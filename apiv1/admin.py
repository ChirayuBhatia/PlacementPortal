from django.contrib import admin
from .models import (Student, Education, Internship, Project, Certificate, Skill, Summary, Language, Accomplishments,
                     CompetitiveExams, )


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


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['student', 'skill']


@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('student', 'summary')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('student', 'language')


@admin.register(CompetitiveExams)
class CompetitiveExamsAdmin(admin.ModelAdmin):
    list_display = ['id']
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


@admin.register(Accomplishments)
class AccomplishmentsAdmin(admin.ModelAdmin):
    list_display = ['id']
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


