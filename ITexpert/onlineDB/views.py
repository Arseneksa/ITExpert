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