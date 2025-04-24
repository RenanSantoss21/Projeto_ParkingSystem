from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vehicles.views import VehicleViewSet, VehicleTypeViewSet

router = DefaultRouter()
router.register('vehicle/type', VehicleTypeViewSet)
router.register('vehicle', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
