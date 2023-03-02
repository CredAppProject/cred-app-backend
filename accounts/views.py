from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from accounts.models import User
from accounts.serializer import UserSerializer,UserProfileSerializer,UserPasswordSerializer


class UserRegistrationAPI(generics.CreateAPIView):
    """API Endpoint for creating a new user"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    """API Endpoint for fetching,updating,deleting the current user."""
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'

class UserList(generics.ListAPIView):
    """API Endpoint for listing all the users - development purpose."""
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserPasswordUpdate(APIView):
    """API Endpoint for updating the password of the user."""
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self,request,*args,**kwargs):
        serializer = UserPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=request.user.id)
            password = serializer.validated_data['old_password']
            if not user.check_password(password):
                #raise error response when old password does not match.
                return Response(data={
                    "status" : "Failed",
                    "message" : "Password does not match",
                },status=status.HTTP_400_BAD_REQUEST)
            
            #hashing and updating the password
            user.set_password(serializer.validated_data['new_password'])
            user.save()

            return Response(data={
                "status" : "Success",
                "message" : "Password updated",
            })       
         
        #handling post data validation errors.
        return Response(data={
            "status" : "Failed",
            "message" : serializer.errors,
        },status=status.HTTP_400_BAD_REQUEST)