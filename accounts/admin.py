from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Cred Admin"
admin.site.register(User)