from accounts.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'name', 'phone', 'profile_picture', 'company', 'job','date_joined']
