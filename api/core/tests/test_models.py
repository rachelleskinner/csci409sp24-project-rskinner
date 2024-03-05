"""
Tests for models.
"""

from django.test import TestCase

from core import models
from datetime import datetime

def create_vessel():
    return models.Vessel.objects.create(
            vessel_name="Vessel NameTest"
        )

class ModelTests(TestCase):

    def test_create_vessel(self):
        """Test Creating a Vessel is Successful."""
        vessel = models.Vessel.objects.create(
            vessel_name="Vessel NameTest"
        )

        self.assertEqual(str(vessel), vessel.vessel_name)
    
    def test_create_vessel_schedule(self):
        """Test Creating a Vessel Schedule is Successful."""
        vessel = create_vessel()
        schedule = models.VesselSchedule.objects.create(
            vessel=vessel,
            voyage_number="Voyage 123",
            arrival_date=datetime.now()
        )

        self.assertEqual(str(schedule), f"{vessel.vessel_name}-{schedule.voyage_number}")

    def test_create_bill_of_lading(self):
        """Test Creating a Bill of Lading is Successful."""
        vessel = create_vessel()
        bol = models.BillOfLading.objects.create(
            voyage=vessel,
            bol_number="BOL 321",
            contact_name="Jane Smith",
            contact_number="5553211234",
            contact_email="email@example.com",
            release_status="R"
        )

        self.assertEqual(str(bol), bol.bol_number)
    
    def test_create_container(self):
        """Test Creating a Container is Successful."""
        vessel = create_vessel()
        bol = models.BillOfLading.objects.create(
            voyage=vessel,
            bol_number="BOL 456",
            contact_name="John Smith",
            contact_number="8009876543",
            contact_email="email@example.com",
            release_status="C"
        )
        container = models.Container.objects.create(
            bol=bol,
            container_number="CONT 456"
        )

        self.assertEqual(str(container), container.container_number)

