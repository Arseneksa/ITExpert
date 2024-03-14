from django.db.models import fields
from rest_framework import serializers
from .models import *
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User

class SiteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Site
        fields = '__all__'
        
class BlockSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Block
        fields = '__all__'
        
class Human_wildlife_conflict_dataSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Human_wildlife_conflict_data
        fields = '__all__'
        
class Human_wildlife_conflict_dataSmartSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Human_wildlife_conflict_dataSmart
        fields = '__all__'