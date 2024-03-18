from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'site', views.SiteViewSet,basename='Site')
router.register(r'block', views.BlockViewSet,basename='Block')
router.register(r'species', views.SpeciesViewSet,basename='Species')
router.register(r'indicators', views.IndicatorViewSet,basename='Indicators')
router.register(r'Human_wildlife_conflict_data', views.Human_wildlife_conflict_dataViewSet,basename='Human_wildlife_conflict_data')
router.register(r'Human_wildlife_conflict_data_smart', views.Human_wildlife_conflict_dataSmartViewSet,basename='Human_wildlife_conflict_data_smart')

router.register(r'wildlife_data', views.Wildlife_dataViewSet,basename='Wildlife_conflict')
router.register(r'wildlife_data_smart', views.Wildlife_dataSmartViewSet,basename='Wildlife_data_smart')

router.register(r'human_pressure_data', views.Human_pressure_dataViewSet,basename='human_pressure_data')
router.register(r'human_pressure_data_smart', views.Human_pressure_dataSmartViewSet,basename='human_pressure_data_smart')

router.register(r'forest_cover_data', views.Forest_cover_dataViewSet,basename='forest_cover_data')
router.register(r'forest_cover_data_smart', views.Forest_cover_dataSmartViewSet,basename='forest_cover_data_smart')

router.register(r'patrol_cover_data', views.Patrol_cover_datatViewSet,basename='patrol_cover_data')
router.register(r'patrol_cover_data_smart', views.Patrol_cover_dataSmartViewSet,basename='patrol_cover_data_smart')

# router.register(r'publicationType', views.PublicationTypeViewSet,basename='PublicationType')
# router.register(r'indicators', views.IndicatorViewSet,basename='Indicator')
# router.register(r'countries', views.CountryViewSet,basename='Country')
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
]