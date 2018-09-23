from rest_framework import routers
from apacheinv.viewsets import httpdinstanceViewSet
router = routers.DefaultRouter()
router.register(r'apache', httpdinstanceViewSet)
