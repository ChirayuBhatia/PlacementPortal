from apiv1.models import Student
from django.db import models


# Create your models here.
class Job(models.Model):
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.URLField()
    package = models.FloatField()

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"


class ApplicationStatus(models.Model):
    class Meta:
        verbose_name = 'Application Status'
        verbose_name_plural = 'Application Status'

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
