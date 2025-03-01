from .serializers import ApplicationSerializer
from .models import ApplicationStatus
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


# Create your views here.
class AppliedList(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicationStatus.objects.filter(
            student__enrollment_no=self.request.user.username
        ).exclude(status='Eligible')


class AvailableJobsList(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicationStatus.objects.filter(
            student__enrollment_no=self.request.user.username,
            status="Eligible"
        )


class ApplyJobView(generics.UpdateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicationStatus.objects.filter(student__enrollment_no=self.request.user.username)
