from django.contrib import admin
from workspace.models import Workspace, SecretKey, SecretFile

# Register your models here.
admin.site.register(Workspace)
admin.site.register(SecretFile)
admin.site.register(SecretKey)
