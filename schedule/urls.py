from django.urls import path
from .views import TimeSlotListCreateView, TimeSlotDetailView

urlpatterns = [
    path('timeslots/', TimeSlotListCreateView.as_view(), name='timeslot-list-create'),
    path('timeslots/<int:pk>/', TimeSlotDetailView.as_view(), name='timeslot-detail'),
]