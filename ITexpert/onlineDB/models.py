from django.db import models
import datetime
from dateutil.relativedelta import relativedelta

#from tkinter.tix import Tree
# Create your models here.

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
    interaction_without_destruction = models.IntegerField(null=True, blank=True)
    interaction_with_destruction = models.IntegerField(null=True, blank=True)
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
        if Human_wildlife_conflict_dataSmart.objects.get(id_hwc_data=self):
            hwc_datasmart = Human_wildlife_conflict_dataSmart.objects.get(id_hwc_data=self)
            hwc_datasmart.site = self.site  
            hwc_datasmart.block = self.block
            hwc_datasmart.year = self.year
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
                                                         end_date = self.collect_end_date,
                                                         monthly_average_rate_intrusion_with_damage=monthly_average_rate_intrusion_with_damage,
                                                         monthly_average_rate_intrusion_without_damage=monthly_average_rate_intrusion_without_damage,
                                                         monthly_average_rate_intrusion=monthly_average_rate_intrusion,
                                                         daily_average_rate_intrusion_with_damage=daily_average_rate_intrusion_with_damage,
                                                         daily_average_rate_intrusion_without_damage=daily_average_rate_intrusion_without_damage,
                                                         daily_average_rate_intrusion=daily_average_rate_intrusion
                                                         )
        
        hwc_datasmart.save()
        super(Human_wildlife_conflict_data, self).save(*args, **kwargs)
    
  
class Human_wildlife_conflict_dataSmart(models.Model):
    
    id_hwc_data = models.ForeignKey(Human_wildlife_conflict_data, on_delete=models.CASCADE, blank=False, null=False)  
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, default=None)  
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, default=None) 
    year = models.IntegerField(choices=year_choices(2010, 1), default=current_year) 
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
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
  
    # def __str__(self) -> str:
        
    #     return self.id