from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from workspace.models import Workspace
from workspace.serializer import WorkspaceSerializer

# Create your views here.
class CustomUserCreation(generics.ListCreateAPIView):
    """API endpoint to create and list all the workspaces"""
    queryset = Workspace.objects.all()
    permission_classes = (IsAuthenticated)
    serializer_class = WorkspaceSerializer