from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    BRANCH_CHOICES = [
        ('IT', 'Information Technology'),
        ('CSE', 'Computer Software Engineering'),
        ('CSE-AIML', 'Computer Software Engineering'),
        ('CSE-DS', 'Computer Software Engineering'),
        ('CSE-BS', 'Computer Software Engineering'),
        ('ECE', 'Electronics & Communication Engineering'),
        ('EX', 'Electrical & Electronics Engineering'),
        ('AU', 'Automobile Engineering'),
        ('ME', 'Mechanical Engineering'),
    ]

    enrollment_no = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE, primary_key=True,
                                         unique=True)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    current_location = models.CharField(max_length=255)
    permanent_address = models.JSONField()
    mobile_number = models.CharField(max_length=15)
    job_status = models.CharField(max_length=50)  # Placed, Unplaced

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.enrollment_no.username


class Skill(models.Model):
    skill = models.JSONField()
    student = models.ForeignKey(Student, to_field='enrollment_no', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class Language(models.Model):
    language = models.JSONField()
    student = models.ForeignKey(Student, to_field='enrollment_no', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"


class Summary(models.Model):
    summary = models.TextField()
    student = models.ForeignKey(Student, to_field='enrollment_no', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Summary"
        verbose_name_plural = "Summary"


class Education(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)
    board_university = models.CharField(max_length=255)
    medium = models.CharField(max_length=50)
    percentage_cgpa = models.CharField(max_length=10)
    school_college_name = models.CharField(max_length=255)
    start_year = models.IntegerField()
    passing_year = models.IntegerField()

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education Records"

    def __str__(self):
        return f"{self.qualification} - {self.board_university}"


class Internship(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company_city = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    skills_used = models.JSONField()

    class Meta:
        verbose_name = "Internship"
        verbose_name_plural = "Internships"

    def __str__(self):
        return f"{self.company_city} Internship"


class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    skills_used = models.JSONField()
    links = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project_name


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    issue_date = models.DateField()
    certificate_id = models.CharField(max_length=255)
    skills_learned = models.JSONField()

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

    def __str__(self):
        return self.certificate_name
