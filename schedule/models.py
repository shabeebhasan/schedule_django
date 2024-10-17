from django.db import models

# Create your models here.
class TimeSlot(models.Model):
    day_of_week = models.CharField(max_length=10)  # e.g., 'monday'
    start_time = models.TimeField()
    end_time = models.TimeField()
    ids = models.JSONField()  # Stores list of IDs associated with the time slot

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.end_time}"