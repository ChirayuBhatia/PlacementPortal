from .serializers import JobSerializer, ApplicationSerializer
from .models import Job, ApplicationStatus
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics


# Create your views here.
class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]


class ApplicationList(generics.ListAPIView):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ApplicationStatus.objects.filter(student__enrollment_no=self.request.user.username)
