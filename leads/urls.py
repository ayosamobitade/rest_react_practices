from rest_framework import routers
from .api import leadViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register("api/leads", leadViewSet, "leads")

urlpatterns = router.urls