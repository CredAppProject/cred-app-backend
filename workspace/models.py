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
    
    
class SecretKey(models.Model):
    workspace = models.ForeignKey(Workspace,on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=1000)
    secret_value = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

class SecretFile(models.Model):
    workspace = models.ForeignKey(Workspace,on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=1000)
    secret_file = models.FileField(upload_to='secret_files')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
