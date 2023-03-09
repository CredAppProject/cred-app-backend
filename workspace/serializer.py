from rest_framework import serializers
from workspace.models import Workspace

class WorkspaceSerializer(serializers.ModelSerializer):
  class Meta:
      model = Workspace
      fields = "__all__"
      read_only_fields  = ('workspace_id',"owner",)