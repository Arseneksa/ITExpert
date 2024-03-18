from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework import serializers, permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from  .models import  *
# Create your views here.

class BlockViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
class SiteViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Site.objects.all()
    

    serializer_class = SiteSerializer
    
class Human_wildlife_conflict_dataViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Human_wildlife_conflict_data.objects.all()
    serializer_class = Human_wildlife_conflict_dataSerializer
class Human_wildlife_conflict_dataSmartViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Human_wildlife_conflict_dataSmart.objects.all()
    

    serializer_class = Human_wildlife_conflict_dataSmartSerializer
    
class IndicatorViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Indicator.objects.all()
    

    serializer_class = IndicatorSerializer
    
class Wildlife_dataViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Wildlife_data.objects.all()
    

    serializer_class = Wildlife_dataSerializer
    
class Wildlife_dataSmartViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Wildlife_dataSmart.objects.all()
    serializer_class = Wildlife_dataSmartSerializer
    
class Human_pressure_dataViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Human_pressure_data.objects.all()
    serializer_class = Human_pressure_dataSerializer
    
class Human_pressure_dataSmartViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Human_pressure_dataSmart.objects.all()
    serializer_class = Human_pressure_dataSmartSerializer
    
class Forest_cover_dataViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Forest_cover_data.objects.all()
    serializer_class = Forest_cover_dataSerializer
    
class Forest_cover_dataSmartViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Forest_cover_dataSmart.objects.all()
    serializer_class = Forest_cover_dataSmartSerializer

class Patrol_cover_datatViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Patrol_cover_data.objects.all()
    serializer_class = Patrol_cover_dataSerializer

class Patrol_cover_dataSmartViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Patrol_cover_dataSmart.objects.all()
    serializer_class = Patrol_cover_dataSmartSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class SamplingViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Sampling.objects.all()
    serializer_class = SamplingSerializer
def index(request):
    
    user=""
    
    if(request.user.is_authenticated):
        if(request.user):
            user = User.objects.get(username =request.user) 
            # print(user)
    context={
       
        'user': user
    }
    
    return render(request, 'index.html',context)