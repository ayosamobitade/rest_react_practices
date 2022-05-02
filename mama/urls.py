from rest_framework import routers
from .api import momoViewSets

router = routers.DefaultRouter()

router.register("api/momo", momoViewSets, "momo")

urlpatterns = router.urls