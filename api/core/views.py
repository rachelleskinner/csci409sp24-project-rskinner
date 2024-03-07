from django.shortcuts import render
from rest_framework import viewsets
from .models import Vessel, VesselSchedule, BillOfLading, Container
from .serializers import VesselSerializer, VesselScheduleSerializer, BillOfLadingSerializer, ContainerSerializer

# Create your views here.
class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer

class VesselScheduleViewSet(viewsets.ModelViewSet):
    queryset = VesselSchedule.objects.all()
    serializer_class = VesselScheduleSerializer

class BillOfLandingViewSet(viewsets.ModelViewSet):
    queryset = BillOfLading.objects.all()
    serializer_class = BillOfLadingSerializer

class Container(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer