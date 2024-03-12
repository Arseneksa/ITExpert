from django.db import models
import datetime
#from tkinter.tix import Tree
# Create your models here.


class Species(models.Model):
    name= models.CharField(max_length=255, blank=True, null=True, default=' ')
    short_name= models.CharField(max_length=255, blank=True, null=True, default=' ')
    scientific_name = models.CharField(max_length=255, blank=True, null=True, default=' ')
    family = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255 , blank=True, null=True, default=' ')
    errorColor = models.CharField(max_length=255 , blank=True, null=True, default=' ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        verbose_name_plural = "species"

    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'none'
class Site(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    short_name = models.CharField(max_length=255,null=False, blank=False)
    color = models.CharField(max_length=255,null=True, blank=True)
    priority = models.BooleanField(default="False")  # type: ignore
    total_area = models.FloatField(null=True, blank=True,verbose_name="Total area (km²)")
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(blank=True, null=True, default=None)
  
    creation_date = models.IntegerField(null=True, blank=True)
    class Meta:
        ordering = ['name']
  
    def __str__(self) -> str:
        if self.name:
            return  '%s'%(self.name)
        else:
            return None 

class Block(models.Model):
    
    name = models.CharField(max_length=255,null=False, blank=False)
    short_name = models.CharField(max_length=255,null=False, blank=False)
    color = models.CharField(max_length=255,null=True, blank=True)
    total_area = models.FloatField(null=True, blank=True,verbose_name="Total area (km²)")
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)  # type: ignore
    
    class Meta:
        ordering = ['name']
  
    def __str__(self) -> str:
        if self.name:
            return  '%s'%(self.name)
        else:
            return None
