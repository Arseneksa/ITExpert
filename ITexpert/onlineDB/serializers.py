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
class IndicatorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Indicator
        fields = '__all__'
        
class Wildlife_dataSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Wildlife_data
        fields = '__all__'

class Wildlife_dataSmartSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Wildlife_dataSmart
        fields = '__all__'

class IndicatorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Indicator
        fields = '__all__'
        
class Forest_cover_dataSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Forest_cover_data
        fields = '__all__'
class Forest_cover_dataSmartSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Forest_cover_dataSmart
        fields = '__all__'

class Patrol_cover_dataSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Patrol_cover_data
        fields = '__all__'
        
class Patrol_cover_dataSmartSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Patrol_cover_dataSmart
        fields = '__all__'
        
class Human_pressure_dataSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Human_pressure_data
        fields = '__all__'
class Human_pressure_dataSmartSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Human_pressure_dataSmart
        fields = '__all__'
        
class SpeciesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Species
        fields = '__all__'
class SamplingSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Sampling
        fields = '__all__'