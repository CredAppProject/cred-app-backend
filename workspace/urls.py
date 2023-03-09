from django.urls import path
from workspace.views import WorkspaceListCreateView

urlpatterns = [
    path("api/v1",WorkspaceListCreateView.as_view(), name='workspace_list_create'),
]