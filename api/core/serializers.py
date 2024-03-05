from rest_framework import serializers
from core.models import Vessel, VesselSchedule, BillOfLading, Container

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ['vessel_name']
        read_only_fields = ['id']

class VesselScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VesselSchedule
        fields = ['vessel', 'voyage_number', 'arrival_date']
        read_only_fields = ['id']

class BillOfLadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfLading
        fields = ['voyage', 'bol_number', 'contact_name', 'contact_number', 'contact_email', 'release_status']
        read_only_fields = ['id']

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ['bol', 'container_number']
        read_only_fields = ['id']