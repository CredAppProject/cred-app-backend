from django.db import models
import uuid

class Workspace(models.Model):
    workspace_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    workspace_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.workspace_name
