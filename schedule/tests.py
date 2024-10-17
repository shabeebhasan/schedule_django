from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import WeeklySchedule, DaySchedule, TimeSlot
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class WeeklyScheduleTests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Obtain JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        
        # Add the token to the client's authentication header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.valid_payload = {
            "monday": {
                "day": "monday",
                "slots": [
                    {
                        "start": "00:00",
                        "stop": "01:00",
                        "ids": [1, 2]
                    },
                    {
                        "start": "01:00",
                        "stop": "02:59",
                        "ids": [3, 4, 5]
                    }
                ]
            },
            "tuesday": {
                "day": "tuesday",
                "slots": [
                    {
                        "start": "00:00",
                        "stop": "23:59",
                        "ids": [6, 7]
                    }
                ]
            },
            "wednesday": {
                "day": "wednesday",
                "slots": [
                    {
                        "start": "00:00",
                        "stop": "23:59",
                        "ids": [8, 9]
                    }
                ]
            }
        }

    # Test POST request for creating a weekly schedule
    def test_create_weekly_schedule(self):
        url = reverse('weeklyschedule-list')
        response = self.client.post(url, self.valid_payload, format='json')
        print(response.data)  # Debugging step to check the actual response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)  # Ensure 'id' is in the response
        self.assertEqual(WeeklySchedule.objects.count(), 1)
        self.assertEqual(DaySchedule.objects.count(), 3)
        self.assertEqual(TimeSlot.objects.count(), 4)

    # Test GET request for retrieving the created weekly schedule
    def test_get_weekly_schedule(self):
        # First, create a schedule
        url = reverse('weeklyschedule-list')
        self.client.post(url, self.valid_payload, format='json')

        # Now, retrieve the schedule
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Expecting 1 schedule

    # Test PUT request to update an existing schedule
    def test_update_weekly_schedule(self):
        # First, create a schedule
        url = reverse('weeklyschedule-list')
        response = self.client.post(url, self.valid_payload, format='json')
        schedule_id = response.data['id']  # Get the ID of the created schedule

        # Prepare data to update
        update_payload = {
            "monday": {
                "day": "monday",
                "slots": [
                    {
                        "start": "10:00",
                        "stop": "12:00",
                        "ids": [20, 21]
                    }
                ]
            },
            "tuesday": {
                "day": "tuesday",
                "slots": [
                    {
                        "start": "10:00",
                        "stop": "12:00",
                        "ids": [30, 31]
                    }
                ]
            }
        }

        update_url = reverse('weeklyschedule-detail', args=[schedule_id])
        response = self.client.put(update_url, update_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DaySchedule.objects.count(), 2)  # Only Monday and Tuesday should exist
        self.assertEqual(TimeSlot.objects.count(), 2)  # Updated time slots count

    # Test DELETE request to delete the schedule
    def test_delete_weekly_schedule(self):
        # First, create a schedule
        url = reverse('weeklyschedule-list')
        response = self.client.post(url, self.valid_payload, format='json')
        schedule_id = response.data['id']  # Get the ID of the created schedule

        # Delete the schedule
        delete_url = reverse('weeklyschedule-detail', args=[schedule_id])
        response = self.client.delete(delete_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(WeeklySchedule.objects.count(), 0)
        self.assertEqual(DaySchedule.objects.count(), 0)
        self.assertEqual(TimeSlot.objects.count(), 0)
