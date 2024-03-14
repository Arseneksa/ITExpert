from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'site', views.SiteViewSet,basename='Site')
router.register(r'block', views.BlockViewSet,basename='Block')
router.register(r'Human_wildlife_conflict_data', views.Human_wildlife_conflict_dataViewSet,basename='Human_wildlife_conflict_data')
router.register(r'Human_wildlife_conflict_data_smart', views.Human_wildlife_conflict_dataSmartViewSet,basename='Human_wildlife_conflict_data_smart')
# router.register(r'publicationType', views.PublicationTypeViewSet,basename='PublicationType')
# router.register(r'indicators', views.IndicatorViewSet,basename='Indicator')
# router.register(r'countries', views.CountryViewSet,basename='Country')
urlpatterns = [
    path('api/', include(router.urls)),
]