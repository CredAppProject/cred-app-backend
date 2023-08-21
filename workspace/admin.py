from django.contrib import admin
from .models import Workspace, SecretKey, SecretFile
from accounts.models import User

class SecretKeyInline(admin.TabularInline):
    model = SecretKey
    extra = 1  # Number of empty forms to display

class SecretFileInline(admin.TabularInline):
    model = SecretFile
    extra = 1  # Number of empty forms to display

class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('workspace_name', 'category', 'owner')
    inlines = [SecretKeyInline, SecretFileInline]

    def save_model(self, request, obj, form, change):
        # Set the owner field to the currently logged-in user
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Only return Workspace objects owned by the currently logged-in user
        queryset = super().get_queryset(request)
        return queryset.filter(owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "owner":
            # Set the default value for the owner field to the currently logged-in user
            kwargs["initial"] = request.user
            kwargs["queryset"] = User.objects.filter(pk=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Workspace, WorkspaceAdmin)

