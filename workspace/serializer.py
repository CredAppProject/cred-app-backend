from rest_framework import serializers
from workspace.models import Workspace, SecretKey, SecretFile

class WorkspaceSerializer(serializers.ModelSerializer):
  class Meta:
      model = Workspace
      fields = "__all__"
      read_only_fields  = ('workspace_id',"owner",)


class SecretKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretKey
        fields = "__all__"
        read_only_fields  = ('workspace_id',"created_by",)


class SecretFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretFile
        fields = "__all__"
        read_only_fields  = ('workspace_id',"created_by",)