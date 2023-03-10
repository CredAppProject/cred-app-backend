from django.urls import path
from workspace.views import WorkspaceListCreateView,WorkspaceGetUpdateDestroyView

urlpatterns = [
    path("api/v1",WorkspaceListCreateView.as_view(), name='workspace_list_create'),
    path("api/v1/<str:id>",WorkspaceGetUpdateDestroyView.as_view(), name='workspace_update_delete'),
]