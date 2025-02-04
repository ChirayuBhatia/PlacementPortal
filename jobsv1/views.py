from .serializers import JobSerializer, ApplicationSerializer
from .models import Job, ApplicationStatus
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


# Create your views here.
class JobList(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ApplicationStatus.objects.filter(student=self.request.user.username).values(
            'job_id', 'job__package', 'job__job_title', 'job__location' 'job__description', 'status'
        )
