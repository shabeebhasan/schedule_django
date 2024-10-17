from django.db import models

# Model to represent a single time slot
class TimeSlot(models.Model):
    start = models.TimeField()  # Start time of the slot
    stop = models.TimeField()   # Stop time of the slot
    ids = models.JSONField(default=list, blank=True, null=True)  # List of IDs for the slot

    def __str__(self):
        return f"{self.start} - {self.stop}"

# Model to represent a schedule for a day
class DaySchedule(models.Model):
    day = models.CharField(max_length=10)  # e.g., 'monday', 'tuesday', etc.
    slots = models.ManyToManyField(TimeSlot)  # Each day can have multiple time slots

    def __str__(self):
        return self.day

# Main schedule model to represent the entire week
class WeeklySchedule(models.Model):
    monday = models.OneToOneField(DaySchedule, on_delete=models.CASCADE, related_name='monday', null=True, blank=True)
    tuesday = models.OneToOneField(DaySchedule, on_delete=models.CASCADE, related_name='tuesday', null=True, blank=True)
    wednesday = models.OneToOneField(DaySchedule, on_delete=models.CASCADE, related_name='wednesday', null=True, blank=True)
    thursday = models.OneToOneField(DaySchedule, on_delete=models.CASCADE, related_name='thursday', null=True, blank=True)
    friday = models.OneToOneField(DaySchedule, on_delete=models.CASCADE, related_name='friday', null=True, blank=True)
    saturday = models.OneToOneField(DaySchedule, on_delete=models.CASCADE, related_name='saturday', null=True, blank=True)
    sunday = models.OneToOneField(DaySchedule, on_delete=models.CASCADE, related_name='sunday', null=True, blank=True)

    def __str__(self):
        return "Weekly Schedule"