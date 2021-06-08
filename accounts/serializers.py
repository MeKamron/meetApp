from rest_framework import serializers
from .models import Profile, Status, Region
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):

    #id orniga username korsatish
    # user = serializers.SerializerMethodField()
    # def get_user(self, obj):
    #   return obj.user.username

    class Meta:
        model = Profile
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = User
        fields = ('id', 'username')