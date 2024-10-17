from rest_framework import serializers
from .models import TimeSlot, DaySchedule, WeeklySchedule

# Serializer for a single time slot
class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['start', 'stop', 'ids']

# Serializer for a single day's schedule
class DayScheduleSerializer(serializers.ModelSerializer):
    slots = TimeSlotSerializer(many=True)

    class Meta:
        model = DaySchedule
        fields = ['day', 'slots']

# Serializer for the entire weekly schedule
class WeeklyScheduleSerializer(serializers.ModelSerializer):
    monday = DayScheduleSerializer(required=False)
    tuesday = DayScheduleSerializer(required=False)
    wednesday = DayScheduleSerializer(required=False)
    thursday = DayScheduleSerializer(required=False)
    friday = DayScheduleSerializer(required=False)
    saturday = DayScheduleSerializer(required=False)
    sunday = DayScheduleSerializer(required=False)

    class Meta:
        model = WeeklySchedule
        fields = ['id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    def create_day_schedule(self, day_data):
        slots_data = day_data.pop('slots', [])
        day_schedule = DaySchedule.objects.create(day=day_data['day'])

        for slot_data in slots_data:
            slot = TimeSlot.objects.create(**slot_data)
            day_schedule.slots.add(slot)  # Add the created slot to the day's schedule

        return day_schedule

    def create(self, validated_data):
        days_data = {
            'monday': validated_data.pop('monday', None),
            'tuesday': validated_data.pop('tuesday', None),
            'wednesday': validated_data.pop('wednesday', None),
            'thursday': validated_data.pop('thursday', None),
            'friday': validated_data.pop('friday', None),
            'saturday': validated_data.pop('saturday', None),
            'sunday': validated_data.pop('sunday', None),
        }

        weekly_schedule = WeeklySchedule.objects.create()

        # Iterate over the days and create their schedules with slots
        for day_name, day_data in days_data.items():
            if day_data:
                day_schedule = self.create_day_schedule(day_data)
                setattr(weekly_schedule, day_name, day_schedule)

        weekly_schedule.save()
        return weekly_schedule
