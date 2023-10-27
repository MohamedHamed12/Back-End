from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import Profile


class CustomRegistration(RegisterSerializer):
    #  first_name = serializers.CharField(write_only=True)
     first_name = serializers.CharField()
     last_name = serializers.CharField()
    #  def custom_signup(self, request, user):
    #      try:
    #          user.first_name = request.data.get("first_name")
    #          user.last_name = request.data.get("last_name")
    #          user.save()
    #      except:
    #          pass


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','first_name', 'last_name', 'bio', 'image')
