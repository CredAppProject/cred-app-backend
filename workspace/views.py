from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from workspace.models import Workspace
from workspace.serializer import WorkspaceSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class WorkspaceListCreateView(generics.ListCreateAPIView):
    """API endpoint to create and list all the workspaces"""
    queryset = Workspace.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkspaceSerializer

    def list(self, request, *args, **kwargs):
        queryset = Workspace.objects.filter(owner=request.user)
        serializer = self.get_serializer(queryset, many=True)

        # modify the response data here
        data = serializer.data
        return Response(data)
        
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)


class WorkspaceGetUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API Endpoint for fetching,updating and deleting invidual models."""
    queryset = Workspace.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkspaceSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'workspace_id'
