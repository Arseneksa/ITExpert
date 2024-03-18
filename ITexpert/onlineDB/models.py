from django.db import models
import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
import numpy as np
import pandas as pd
import scipy.stats as st
#from tkinter.tix import Tree
# Create your models here.
np.seterr(divide='ignore', invalid='ignore')

def year_choices(start, incr):

    return [(r, r) for r in range(start, datetime.date.today().year+incr, incr)]
def current_year():
    return datetime.date.today().year

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

class Sampling(models.Model):
    
    size = models.IntegerField(null=True, blank=True)
    sampling_method = models.CharField(max_length=255,null=False, blank=False)
    description = models.TextField(max_length=255,null=False, blank=False)
    # color = models.CharField(max_length=255,null=True, blank=True)
    # total_area = models.FloatField(null=True, blank=True,verbose_name="Total area (km²)")
    # longitude = models.FloatField(null=True, blank=True)
    # latitude = models.FloatField(null=True, blank=True)
    # site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)  # type: ignore
    
    class Meta:
        ordering = ['sampling_method']
        verbose_name_plural = "sampling"
  
    def __str__(self) -> str:
        if self.sampling_method:
            return  '%s'%(self.sampling_method)
        else:
            return None

class Indicator(models.Model):
    pillars = [
        ("Human wildlife conflict","Human wildlife conflict"),
        ("Wildlife survey","Wildlife survey"),
        ("Human activity","Human activity"),
        ("Spatial data and landcover","Spatial data and landcover"),
    ]
    name = models.CharField(max_length=255,null=False, blank=False)
    description = models.TextField(max_length=255,null=False, blank=False)
    color = models.CharField(max_length=255,null=True, blank=True)
    var_name = models.CharField(max_length=255,null=True, blank=True)
    pillar = models.CharField(max_length=255,choices=pillars, default=current_year)
    
    class Meta:
        ordering = ['name']
  
    def __str__(self) -> str:
        if self.name:
            return  '%s'%(self.name)
        else:
            return None
def days_between(d1, d2):
    # d1 = datetime.strptime(d1, "%Y-%m-%d")
    # d2 = datetime.strptime(d2, "%Y-%m-%d")
    return int(abs((d2 - d1).days))
def month_between(d1, d2):
    # d1 = datetime.date(d1, "%Y-%m-%d")
    # d2 = datetime.date(d2, "%Y-%m-%d")
    print(abs((d1 - d2).days))
    # difference_jours = abs((d2 - d1).days)
    # diff = relativedelta.relativedelta(end, start)
    # diff_in_months = diff.months + diff.years * 12
    result = int(abs((d1 - d2).days)//30)
    # print(result)
    return result
class Human_wildlife_conflict_data(models.Model):
    
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=False, null=False)  
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    collect_start_date = models.DateField(null=False, blank=False)
    collect_end_date = models.DateField(null=False, blank=False)
    data_level = models.CharField(max_length=255,null=False, blank=False, default="year")
    interaction_without_destruction = models.IntegerField(null=True, blank=False,default=0)
    interaction_with_destruction = models.IntegerField(null=True, blank=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Human wildlife conflict data"
    # Override save function to add Human_wildlife_conflict_dataSmart indicator
    def save(self, *args, **kwargs):
        total_intrusion = self.interaction_with_destruction + self.interaction_without_destruction
        nb_month = month_between(self.collect_end_date,self.collect_start_date)
        nb_days = days_between(self.collect_end_date,self.collect_start_date)
        monthly_average_rate_intrusion_with_damage = round((self.interaction_with_destruction/total_intrusion/nb_month)*100,2)
        monthly_average_rate_intrusion_without_damage = round((self.interaction_without_destruction/total_intrusion/nb_month)*100,2)
        monthly_average_rate_intrusion =round((monthly_average_rate_intrusion_with_damage+monthly_average_rate_intrusion_without_damage),2)
        daily_average_rate_intrusion_with_damage = round((self.interaction_with_destruction/total_intrusion/nb_days)*100,2)
        daily_average_rate_intrusion_without_damage = round((self.interaction_without_destruction/total_intrusion/nb_days)*100,2)
        daily_average_rate_intrusion=round((daily_average_rate_intrusion_with_damage+daily_average_rate_intrusion_without_damage),2)
        qs = Human_wildlife_conflict_dataSmart.objects.filter(id_hwc_data=self)
        if len(qs) > 0 :
            hwc_datasmart = qs.first()
            hwc_datasmart.site = self.site  
            hwc_datasmart.block = self.block
            hwc_datasmart.year = self.year
            hwc_datasmart.data_level = self.data_level
            hwc_datasmart.start_date = self.collect_start_date
            hwc_datasmart.end_date = self.collect_end_date
            hwc_datasmart.monthly_average_rate_intrusion_with_damage = monthly_average_rate_intrusion_with_damage
            hwc_datasmart.monthly_average_rate_intrusion_without_damage = monthly_average_rate_intrusion_without_damage
            hwc_datasmart.monthly_average_rate_intrusion = monthly_average_rate_intrusion
            hwc_datasmart.daily_average_rate_intrusion_with_damage = daily_average_rate_intrusion_with_damage
            hwc_datasmart.daily_average_rate_intrusion_without_damage = daily_average_rate_intrusion_without_damage
            hwc_datasmart.daily_average_rate_intrusion=daily_average_rate_intrusion
            
        else:
            
            hwc_datasmart= Human_wildlife_conflict_dataSmart(id_hwc_data=self,site=self.site,block=self.block,year=self.year,start_date=self.collect_start_date,
                                                         end_date = self.collect_end_date,data_level=self.data_level,
                                                         monthly_average_rate_intrusion_with_damage=monthly_average_rate_intrusion_with_damage,
                                                         monthly_average_rate_intrusion_without_damage=monthly_average_rate_intrusion_without_damage,
                                                         monthly_average_rate_intrusion=monthly_average_rate_intrusion,
                                                         daily_average_rate_intrusion_with_damage=daily_average_rate_intrusion_with_damage,
                                                         daily_average_rate_intrusion_without_damage=daily_average_rate_intrusion_without_damage,
                                                         daily_average_rate_intrusion=daily_average_rate_intrusion
                                                         )
        super(Human_wildlife_conflict_data, self).save(*args, **kwargs)
        hwc_datasmart.save()
        
    
  
class Human_wildlife_conflict_dataSmart(models.Model):
    
    id_hwc_data = models.ForeignKey(Human_wildlife_conflict_data, on_delete=models.CASCADE, blank=False, null=False)  
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None) 
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year) 
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    data_level = models.CharField(max_length=255,null=False, blank=False, default="year")
    monthly_average_rate_intrusion_with_damage = models.FloatField(null=True, blank=True)
    monthly_average_rate_intrusion_without_damage = models.FloatField(null=True, blank=True)
    monthly_average_rate_intrusion = models.FloatField(null=True, blank=True)
    daily_average_rate_intrusion_with_damage = models.FloatField(null=True, blank=True)
    daily_average_rate_intrusion_without_damage = models.FloatField(null=True, blank=True)
    daily_average_rate_intrusion = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Human wildlife conflict data smart"
  
def confident_interval_generator(model_data,model_data_smart,levels,level_value,self,indicator):
    for level in levels:
            qs = model_data_smart.objects.filter(year=self.year,level =level.replace("_id",""),block=self.block,site=self.site,species=self.species)
            if len(qs) > 0 :
                data = list(model_data.objects.filter(year=self.year ).values())
                df = pd.DataFrame(data)
                datasmart = qs.first()
                df = df.loc[(df[level]==level_value[level])&(df["species_id"]==self.species.id)]
                # print(df.columns)
                if len(df[indicator] < 30):
                    interval =st.t.interval(
                    confidence=0.95,
                    df=len(df[indicator])-1,
                    loc=np.mean(df[indicator]),
                    scale=st.sem(df[indicator]))
                else:
                    interval =st.norm.interval(
                        confidence=0.95,
                        loc=np.mean(df[indicator]),
                        scale=st.sem(df[indicator]))
                # encounter_rate_min,encounter_rate_max =interval
                datasmart.level  = level.replace("_id","")
                datasmart.species = self.species
                datasmart.site = self.site
                datasmart.block =self.block
                datasmart.year = self.year  
                if indicator=="encounter_rate":
                    encounter_rate_min,encounter_rate_max =interval
                    datasmart.encounter_rate = round(np.mean(df[indicator]),2)
                    datasmart.encounter_rate_min = round(encounter_rate_min,2)
                    datasmart.encounter_rate_max = round(encounter_rate_max,2)
                if indicator=="forest_cover_rate":
                    forest_cover_rate_min,forest_cover_rate_max =interval
                    datasmart.forest_cover_rate = round(np.mean(df[indicator]),2)
                    datasmart.forest_cover_rate_min = round(forest_cover_rate_min,2)
                    datasmart.forest_cover_rate_max = round(forest_cover_rate_max,2)
                if indicator=="patrol_cover_rate":
                    patrol_cover_rate_min,patrol_cover_rate_max =interval
                    datasmart.patrol_cover_rate = round(np.mean(df[indicator]),2)
                    datasmart.patrol_cover_rate_min = round(patrol_cover_rate_min,2)
                    datasmart.patrol_cover_rate_max = round(patrol_cover_rate_max,2)
                datasmart.save()
            else:
                
                data = list(model_data.objects.filter(year=self.year).values())
                df = pd.DataFrame(data)
                
                # print(df.columns)
                # level =self.level 
                for level in levels:
                    datasmart = model_data_smart()
                    datasmart.level  = level.replace("_id","")
                    datasmart.species = self.species
                    datasmart.site = self.site
                    datasmart.block =self.block
                    datasmart.year = self.year 
                    if indicator=="encounter_rate":
                        encounter_rate_min=encounter_rate_max =round(self.encounter_rate,2)
                        datasmart.encounter_rate = round(self.encounter_rate,2)
                        datasmart.encounter_rate_min = encounter_rate_min
                        datasmart.encounter_rate_max = encounter_rate_max
                    if indicator=="forest_cover_rate":
                        forest_cover_rate_min=forest_cover_rate_max =self.forest_cover_rate
                        datasmart.forest_cover_rate = round(self.forest_cover_rate,2)
                        datasmart.forest_cover_rate_min = round(forest_cover_rate_min,2)
                        datasmart.forest_cover_rate_max = round(forest_cover_rate_max,2)
                    if indicator=="patrol_cover_rate":
                        patrol_cover_rate_min=patrol_cover_rate_max =self.patrol_cover_rate
                        datasmart.patrol_cover_rate = round(self.patrol_cover_rate,2)
                        datasmart.patrol_cover_rate_min = round(patrol_cover_rate_min,2)
                        datasmart.patrol_cover_rate_max = round(patrol_cover_rate_max,2)
                
                    datasmart.save()
class Wildlife_data(models.Model):
    level = [
        ("site","site"),
        ("block","block"),
    ]
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year,null=False)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False, null=False)  
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)   
    sampling = models.ForeignKey(Sampling, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    # level = models.CharField(max_length=255,null=False, blank=False, default="block")
    encounter_rate = models.FloatField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Wildlife data"
    # Override save function to add Human_wildlife_conflict_dataSmart indicator
    def save(self, *args, **kwargs):
        level_value = {
            "block_id":self.block.id,
            "site_id":self.site.id
        }
        levels = {
            "block_id",
            "site_id"
        }
        super(Wildlife_data, self).save(*args, **kwargs)
        confident_interval_generator(Wildlife_data,Wildlife_dataSmart,levels,level_value,self,"encounter_rate")
    
  
class Wildlife_dataSmart(models.Model):
    
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False, null=False) 
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None) 
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year) 
   
    level = models.CharField(max_length=255,null=False, blank=False, default="block")
    encounter_rate_min = models.FloatField(null=True, blank=True)
    encounter_rate_max = models.FloatField(null=True, blank=True)
    encounter_rate = models.FloatField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Wildlife data smart"


class Human_pressure_data(models.Model):
    level = [
        ("site","site"),
        ("block","block"),
    ]
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year,null=False)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False, null=False)  
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)   
    sampling = models.ForeignKey(Sampling, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    # level = models.CharField(max_length=255,null=False, blank=False, default="block")
    encounter_rate = models.FloatField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Human pressure data"
    # Override save function to add Human_wildlife_conflict_dataSmart indicator
    def save(self, *args, **kwargs):
        level_value = {
            "block_id":self.block.id,
            "site_id":self.site.id
        }
        levels = {
            "block_id",
            "site_id"
        }
        super(Human_pressure_data, self).save(*args, **kwargs)
        
        confident_interval_generator(Human_pressure_data,Human_pressure_dataSmart,levels,level_value,self,"encounter_rate")
        
    
  
class Human_pressure_dataSmart(models.Model):
    
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False, null=False) 
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None) 
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year) 
   
    level = models.CharField(max_length=255,null=False, blank=False, default="block")
    encounter_rate_min = models.FloatField(null=True, blank=True)
    encounter_rate_max = models.FloatField(null=True, blank=True)
    encounter_rate = models.FloatField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Human pressure data smart"
class Forest_cover_data(models.Model):
    level = [
        ("site","site"),
        ("block","block"),
    ]
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year,null=False)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False, null=False)  
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)   
    sampling = models.ForeignKey(Sampling, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    # level = models.CharField(max_length=255,null=False, blank=False, default="block")
    forest_cover_rate = models.FloatField(null=False, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Forest cover data"
    # Override save function to add Human_wildlife_conflict_dataSmart indicator
    def save(self, *args, **kwargs):
        level_value = {
            "block_id":self.block.id,
            "site_id":self.site.id
        }
        levels = {
            "block_id",
            "site_id"
        }
        super(Forest_cover_data, self).save(*args, **kwargs)
        
        confident_interval_generator(Forest_cover_data,Forest_cover_dataSmart,levels,level_value,self,"forest_cover_rate")
        
    
  
class Forest_cover_dataSmart(models.Model):
    
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False, null=False) 
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None) 
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year) 
   
    level = models.CharField(max_length=255,null=False, blank=False, default="block")
    forest_cover_rate_min = models.FloatField(null=True, blank=True)
    forest_cover_rate_max = models.FloatField(null=True, blank=True)
    forest_cover_rate = models.FloatField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Forest cover data smart"

class Patrol_cover_data(models.Model):
    level = [
        ("site","site"),
        ("block","block"),
    ]
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year,null=False)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False, null=False)  
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)   
    sampling = models.ForeignKey(Sampling, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    # level = models.CharField(max_length=255,null=False, blank=False, default="block")
    patrol_cover_rate = models.FloatField(null=False, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Patrol cover data"
    # Override save function to add Human_wildlife_conflict_dataSmart indicator
    def save(self, *args, **kwargs):
        level_value = {
            "block_id":self.block.id,
            "site_id":self.site.id
        }
        levels = {
            "block_id",
            "site_id"
        }
        super(Patrol_cover_data, self).save(*args, **kwargs)
        
        confident_interval_generator(Patrol_cover_data,Patrol_cover_dataSmart,levels,level_value,self,"patrol_cover_rate")
        
    
  
class Patrol_cover_dataSmart(models.Model):
    
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False, null=False) 
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None) 
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year) 
   
    level = models.CharField(max_length=255,null=False, blank=False, default="block")
    patrol_cover_rate_min = models.FloatField(null=True, blank=True)
    patrol_cover_rate_max = models.FloatField(null=True, blank=True)
    patrol_cover_rate = models.FloatField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['year']
        verbose_name_plural = "Patrol cover data smart"







