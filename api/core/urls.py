from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VesselViewSet, VesselScheduleViewSet, BillOfLandingViewSet, ContainerViewSet

router = DefaultRouter()
router.register(r'vessels', VesselViewSet)
router.register(r'vessel_schedules', VesselScheduleViewSet)
router.register(r'bill_of_landings', BillOfLandingViewSet)
router.register(r'containters', ContainerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]