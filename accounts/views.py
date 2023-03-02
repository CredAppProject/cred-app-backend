from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from accounts.models import User
from accounts.serializer import UserSerializer


class UserRegistrationAPI(generics.CreateAPIView):
    """API Endpoint for creating a new user"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    """API Endpoint for fetching,updating,deleting the current user."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'

    # def get(self,request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     # make sure to catch 404's below
    #     obj = queryset.get(pk=self.request.user.id)
    #     print(obj)
    #     self.check_object_permissions(self.request, obj)
    #     return obj
