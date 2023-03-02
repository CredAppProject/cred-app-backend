from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from accounts.models import User
from accounts.serializer import UserSerializer,UserProfileSerializer


class UserRegistrationAPI(generics.CreateAPIView):
    """API Endpoint for creating a new user"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    """API Endpoint for fetching,updating,deleting the current user."""
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'

class UserList(generics.ListAPIView):
    """API Endpoint for listing all the users - development purpose."""
    serializer_class = UserSerializer
    queryset = User.objects.all()