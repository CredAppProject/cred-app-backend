from django.db import models
from accounts.models import User
import uuid

class Workspace(models.Model):
    workspace_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    workspace_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.workspace_name
