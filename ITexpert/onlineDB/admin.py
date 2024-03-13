from django.contrib import admin
from  .models import  *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.
    
    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """
    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return '-'
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f'admin:{app_label}_{model_name}_change'
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify
admin.site.site_header = ' IT_EXPERT  Administration'


class SiteResource(resources.ModelResource):

    class Meta:
        model = Site
class BlockResource(resources.ModelResource):

    class Meta:
        model = Block
        exclude = ('created_at', 'updated_at',)
        
class Human_wildlife_conflict_dataSmartResource(resources.ModelResource):

    class Meta:
        model = Human_wildlife_conflict_dataSmart
class Human_wildlife_conflict_dataResource(resources.ModelResource):

    class Meta:
        model = Human_wildlife_conflict_data
        exclude = ('created_at', 'updated_at',)





@admin.register(Block)
class BlockAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("id",linkify(field_name="site"), "latitude", "longitude", "total_area", "color", "short_name", "name")
    resource_class = BlockResource
    search_fields = ('name','id',)
@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("id", "short_name", "name", "image", "description", "latitude", "longitude", "total_area", "priority", "color")
    resource_class = SiteResource
    search_fields = ('name','id',)





@admin.register(Human_wildlife_conflict_data)
class Human_wildlife_conflict_dataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ( "id", linkify(field_name="site"), linkify(field_name="block"), "year","collect_end_date", "collect_start_date", "interaction_with_destruction", "interaction_without_destruction")
    search_fields = ('site','id',"block","year")
    resource_class = Human_wildlife_conflict_dataResource
    


@admin.register(Human_wildlife_conflict_dataSmart)
class Human_wildlife_conflict_dataSmartAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("id",linkify(field_name="id_hwc_data"), linkify(field_name="site"),linkify(field_name="block"),  "year","start_date","end_date", "daily_average_rate_intrusion", "daily_average_rate_intrusion_without_damage", "daily_average_rate_intrusion_with_damage", "monthly_average_rate_intrusion", "monthly_average_rate_intrusion_without_damage", "monthly_average_rate_intrusion_with_damage")
    search_fields = ('site','id',"block","year")
    resource_class = Human_wildlife_conflict_dataSmartResource