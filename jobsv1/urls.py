from django.urls import path
from .views import JobList, ApplicationList

urlpatterns = [
    path('job_list', JobList.as_view(), name='JobList'),
    path('application_list', ApplicationList.as_view(), name='ApplicationList'),
]
