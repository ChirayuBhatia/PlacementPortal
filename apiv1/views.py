from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework import generics
import json


# Create your views here.
def index(request):
    data = json.loads(request.body)
    print(data)
    return HttpResponse("Hello World")


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
