from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = "Cred App Dashboard"

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone','profile_picture', 'date_joined', 'company', "job")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(id=request.user.id)  # Assuming there's a ForeignKey to User in YourModel.

admin.site.register(User, YourModelAdmin)
