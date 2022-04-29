from rest_framework import routers

from leads.api import leadViewSet
from .api import boboViewset
from django.urls import path

router = routers.DefaultRouter()

router.register("api/bobo", boboViewset, "bobo")

urlpatterns = router.urls