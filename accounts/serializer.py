from accounts.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','email', 'password','name', 'phone', 'profile_picture', 'company', 'job','date_joined']
    read_only_fields  = ('id',)