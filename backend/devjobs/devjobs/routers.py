from rest_framework import routers
from job.viewsets import JobViewSet

router = routers.DefaultRouter()

router.register(r'job', JobViewSet)
