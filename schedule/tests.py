from django.test import TestCase
from .models import TimeSlot

# Create your tests here.

class TimeSlotTestCase(TestCase):
    def setUp(self):
        TimeSlot.objects.create(day_of_week="monday", start_time="00:00", end_time="01:00", ids=[1, 2])

    def test_timeslot_creation(self):
        monday_slot = TimeSlot.objects.get(day_of_week="monday")
        self.assertEqual(monday_slot.ids, [1, 2])