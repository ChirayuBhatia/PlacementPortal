from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.decorators import login_required
from .views import index, RegisterUserView
from django.urls import path

urlpatterns = [
    path('', login_required(index), name='index'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
