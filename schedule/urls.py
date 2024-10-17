from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeeklyScheduleViewSet

router = DefaultRouter()
router.register(r'weekly-schedules', WeeklyScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]