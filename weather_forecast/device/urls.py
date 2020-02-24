"""URLs for device application."""

from django.urls import path, include
from rest_framework_nested import routers

from .views import DeviceViewSet, DataViewSet

router = routers.SimpleRouter()
router.register(r'', DeviceViewSet)

data_router = routers.NestedSimpleRouter(router, r'', lookup='device')
data_router.register(r'data', DataViewSet, basename='device-data')

urlpatterns = [
    path("/", include(router.urls)),
    path("/", include(data_router.urls)),
]
