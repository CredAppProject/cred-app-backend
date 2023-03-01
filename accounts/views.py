from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from accounts.models import User
from accounts.serializer import UserSerializer


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
