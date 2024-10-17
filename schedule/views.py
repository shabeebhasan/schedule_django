from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import WeeklySchedule
from .serializers import WeeklyScheduleSerializer

# ViewSet for managing weekly schedules
class WeeklyScheduleViewSet(viewsets.ModelViewSet):
    queryset = WeeklySchedule.objects.all()
    serializer_class = WeeklyScheduleSerializer
    permission_classes = [IsAuthenticated]  # JWT auth requirement

    def create(self, request, *args, **kwargs):
        # Use the default create method to ensure the response includes the 'id' field
        response = super().create(request, *args, **kwargs)
        return response