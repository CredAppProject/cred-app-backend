from django.urls import path
from accounts.views import *

urlpatterns = [
    path("api/v1",hello)
]