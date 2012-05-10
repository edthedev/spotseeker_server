from django.conf import settings
from django.utils import unittest
from django.test.client import Client
from spotseeker_server.models import Spot, SpotAvailableHours

class SpotHoursOverlapTest(unittest.TestCase):
    """ Tests that when open hours are submitted that overlap with other open hours for a Spot, the previous Spot hours are adjusted rather than having multiple AvailableHours hanging around.
    """
    def setUp(self):
        spot = Spot.objects.create(name="This spot has overlapping hours")
        self.spot = spot

    def test_early_overlap(self):
        """ Tests adding SpotAvailableHours with a start time earlier than an existing start, but end within the current open hours.
        """
        hours1 = SpotAvailableHours.objects.create(spot=self.spot, day="m", start_time="09:00", end_time="12:00")
        hours2 = SpotAvailableHours.objects.create(spot=self.spot, day="m", start_time="07:00", end_time="10:00")

        # creating hours2 should get those times merged into hours1
        hours_obj_count = self.spot.spotavailablehours_set.values_list().count()
        self.assertEquals(hours_obj_count, 1, "Only one SpotAvailableHours object")
        
        # check to see that start and end times are correct
        new_hours = self.spot.spotavailablehours_set.values_list()[0]
        self.assertEquals(hours2.start_time, new_hours.start_time, "Start time is the same")
        self.assertEquals(hours1.end_time, new_hours.end_time, "End time is the same")

    def test_late_overlap(self):
        """ Tests adding SpotAvailableHours with a start time within current hours, but an end time later than the current open hours.
        """
        hours1 = SpotAvailableHours.objects.create(spot=self.spot, day="m", start_time="09:00", end_time="12:00")
        hours2 = SpotAvailableHours.objects.create(spot=self.spot, day="m", start_time="10:00", end_time="14:00")

        # creating hours2 should get those times merged into hours1
        hours_obj_count = self.spot.spotavailablehours_set.values_list().count()
        self.assertEquals(hours_obj_count, 1, "Only one SpotAvailableHours object")
        
        # check to see that start and end times are correct
        new_hours = self.spot.spotavailablehours_set.values_list()[0]
        self.assertEquals(hours1.start_time, new_hours.start_time, "Start time is the same")
        self.assertEquals(hours2.end_time, new_hours.end_time, "End time is the same")

    def test_total_overlap(self):
        pass

    def test_underlap(self):
        pass

    def test_no_overlap(self):
        pass

    def test_exact_same_start(self):
        pass

    def test_exact_same_end(self):
        pass

    def test_exact_same_hours(self):
        pass
