from django.urls import path
from workspace.views import WorkspaceListCreateView,WorkspaceGetUpdateDestroyView, SecretKeyListCreateView, SecretKeyGetUpdateDestroyView, SecretFileGetUpdateDestroyView, SecretFileListCreateView

urlpatterns = [
    path("api/v1",WorkspaceListCreateView.as_view(), name='workspace_list_create'),
    path("api/v1/<str:id>",WorkspaceGetUpdateDestroyView.as_view(), name='workspace_update_delete'),
    path("api/v1/keys/<str:workspace_id>",SecretKeyListCreateView.as_view(), name='workspace_list_create'),
    path("api/v1/key/<str:secret_id>",SecretKeyGetUpdateDestroyView.as_view(), name='workspace_update_delete'),
    path("api/v1/files/<str:workspace_id>",SecretFileListCreateView.as_view(), name='workspace_list_create'),
    path("api/v1/file/<str:secret_id>",SecretFileGetUpdateDestroyView.as_view(), name='workspace_update_delete'),
]