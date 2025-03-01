from django.urls import path
from .views import AppliedList, AvailableJobsList, ApplyJobView

urlpatterns = [
    path('job_list/', AvailableJobsList.as_view(), name='JobList'),
    path('application_list/', AppliedList.as_view(), name='ApplicationList'),
    path('apply_job/', ApplyJobView.as_view(), name='ApplyJob'),
]
