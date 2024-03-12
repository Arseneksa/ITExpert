from django.contrib import admin
from  .models import  *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.



admin.site.site_header = ' IT_EXPERT  Administration'


class SiteResource(resources.ModelResource):

    class Meta:
        model = Site
class BlockResource(resources.ModelResource):

    class Meta:
        model = Block
        exclude = ('created_at', 'updated_at',)





@admin.register(Block)
class BlockAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("id","site", "latitude", "longitude", "total_area", "color", "short_name", "name")
    resource_class = BlockResource
    search_fields = ('name','id',)
@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("id", "short_name", "name", "image", "description", "latitude", "longitude", "total_area", "priority", "color")
    resource_class = SiteResource
    search_fields = ('name','id',)