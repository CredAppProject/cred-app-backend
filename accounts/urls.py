from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import UserRegistrationAPI,UserProfileAPI

urlpatterns = [
    path("api/auth/v1/login",TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/auth/v1/login/refresh",TokenRefreshView.as_view(), name='token_refresh'),
    path("api/auth/v1/create",UserRegistrationAPI.as_view()),
    path("api/auth/v1/<str:pk>",UserProfileAPI.as_view(),name="user-profile"),
]