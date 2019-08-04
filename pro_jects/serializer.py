from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model=Profile
    fields = ('prof_pic','bio','contact','name')

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model=Project
    fields = ('image','name','description','link')
