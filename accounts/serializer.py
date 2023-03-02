from accounts.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','email', 'password','name', 'phone', 'profile_picture', 'company', 'job','date_joined']
    read_only_fields  = ('id',)
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    """To create a new auth.user model"""
    user = User.objects.create_user(**validated_data)
    user.save()
    return user