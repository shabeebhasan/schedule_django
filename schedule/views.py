from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import TimeSlot
from .serializers import TimeSlotSerializer
from rest_framework.permissions import IsAuthenticated

class TimeSlotListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer

class TimeSlotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer