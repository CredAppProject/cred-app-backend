from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenBlacklistView
)
from accounts.views import UserRegistrationAPI,UserProfileAPI,UserList,UserPasswordUpdate

urlpatterns = [
    path("api/auth/v1/login",TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/auth/v1/login/refresh",TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/v1/logout', TokenBlacklistView.as_view(), name='token_blacklist'),

    path("api/auth/v1/create",UserRegistrationAPI.as_view()),
    path("api/auth/v1/profile/<str:pk>",UserProfileAPI.as_view(),name="user-profile"),

    path("api/auth/v1/change_password",UserPasswordUpdate.as_view(),name="change-password"),

    #development purpose
    path("api/auth/users",UserList.as_view()),
]